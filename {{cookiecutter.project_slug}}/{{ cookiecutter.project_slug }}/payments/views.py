import logging
import jwt
from jwt.exceptions import DecodeError
from stripe.error import StripeError, CardError
from stripe import Customer as StripeCustomer

from pinax.stripe.models import Customer
from pinax.stripe.actions.customers import sync_customer
from pinax.stripe.views import PaymentMethodCreateView, SubscriptionUpdateView, PaymentMethodUpdateView
from pinax.stripe.actions.sources import sync_payment_source_from_stripe_data, delete_card
from pinax.stripe.mixins import LoginRequiredMixin

from django import forms
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.utils.encoding import smart_str
from django.conf import settings
from django.views.generic import FormView
from django.shortcuts import redirect
from django.core.urlresolvers import reverse
from django.contrib import messages
from django.http import HttpResponseRedirect

from {{ cookiecutter.project_slug }}.payments.plan import get_plans

logger = logging.getLogger(__name__)


class CustomSubscriptionUpdateView(SubscriptionUpdateView):

    def get_context_data(self, **kwargs):
        data = super(CustomSubscriptionUpdateView, self).get_context_data(**kwargs)
        data["plans"] = get_plans()
        data["change_button"] = True
        return data

    def update_subscription(self, plan_id):
        super(CustomSubscriptionUpdateView, self).update_subscription(plan_id)
        #deactivate_exceeding_private_repos.delay(self.request.user.pk)


class CustomPaymentMethodCreateView(PaymentMethodCreateView):

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        if self.customer is None:
            messages.error(request, "You can't add a card without a subscription")
            return HttpResponseRedirect(reverse("pinax_stripe_subscription_list"))
        return super(CustomPaymentMethodCreateView, self).dispatch(request, *args, **kwargs)

    def create_card(self, stripe_token):
        for card in self.customer.card_set.all():
            delete_card(self.customer, card.stripe_id)
        source = self.customer.stripe_customer.sources.create(source=stripe_token)
        sync_payment_source_from_stripe_data(self.customer, source)

    def post(self, request, *args, **kwargs):
        try:
            self.create_card(request.POST.get("stripeToken"))
            return redirect("pinax_stripe_subscription_list")
        except CardError as e:
            return self.render_to_response(self.get_context_data(errors=smart_str(e)))


class OctobatForm(forms.Form):

    transactionDetails = forms.CharField()

    def clean_transactionDetails(self):
        details = self.cleaned_data["transactionDetails"]
        try:
            data = jwt.decode(details, settings.OCTOBAT_PRIVATE_KEY)
            customer = data["customer_id"]
            return data
        except DecodeError as e:
            logger.error("Unable to clean transactionDetails for data: {}".format(
                details
            ), exc_info=True)
            raise forms.ValidationError("transaction details could'nt be received")
        except KeyError as e:
            logger.error("Unable to clean transactionDetails for data: {}".format(
                details
            ), exc_info=True)
            raise forms.ValidationError("transaction details could'nt be received")


class CheckoutView(LoginRequiredMixin, FormView):

    form_class = OctobatForm
    template_name = "pinax/stripe/subscription_create.html"

    def get_context_data(self, **kwargs):
        data = super(CheckoutView, self).get_context_data(**kwargs)
        data["plans"] = get_plans()
        data["OCTOBAT_PUBLIC_KEY"] = settings.OCTOBAT_PUBLIC_KEY
        data["OCTOBAT_SUPPLIER_NAME"] = settings.OCTOBAT_SUPPLIER_NAME
        data["OCTOBAT_IMAGE"] = settings.OCTOBAT_IMAGE
        data["octobat_button"] = True
        return data

    def form_valid(self, form):
        trans = form.cleaned_data["transactionDetails"]
        try:
            stripe_customer = StripeCustomer.retrieve(trans["customer_id"])
            cus = Customer.objects.create(
                user=self.request.user,
                stripe_id=stripe_customer["id"]
            )
            sync_customer(cus, stripe_customer)
            return redirect(reverse("pinax_stripe_subscription_list"))
        except StripeError as e:
            messages.error(self.request, "Unable to communicate with stripe. Please try again later")
            logger.error("Stripe Error during checkout for customer {}".format(
                self.request.user
            ), exc_info=True)
            return redirect(reverse("pinax_stripe_subscription_list"))

    def form_invalid(self, form):
        messages.error(self.request,
                       "Unable to process request. Please contact support.")
        return super(CheckoutView, self).form_invalid(form)

    def dispatch(self, request, *args, **kwargs):
        if not self.request.user.is_anonymous():
            if self.request.user.is_customer:
                messages.add_message(request, messages.ERROR, "You already have a subscription")
                return redirect(reverse("pinax_stripe_subscription_list"))
        return super(CheckoutView, self).dispatch(request, *args, **kwargs)
