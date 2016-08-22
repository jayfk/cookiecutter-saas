from pinax.stripe import views as pinax_views

from django.conf.urls import url
from django.views.generic import TemplateView, RedirectView
from django.core.urlresolvers import reverse_lazy

from . import views

urlpatterns = [
    url(r"^subscriptions/$", pinax_views.SubscriptionListView.as_view(), name="pinax_stripe_subscription_list"),
    url(r"^checkout/$", views.CheckoutView.as_view(), name="pinax_stripe_subscription_create"),
    url(r"^subscriptions/(?P<pk>\d+)/delete/$", pinax_views.SubscriptionDeleteView.as_view(), name="pinax_stripe_subscription_delete"),
    url(r"^subscriptions/(?P<pk>\d+)/update/$",views.CustomSubscriptionUpdateView.as_view(), name="pinax_stripe_subscription_update"),
    url(r"^payment-methods/create/$", views.CustomPaymentMethodCreateView.as_view(), name="pinax_stripe_payment_method_create"),
    url(r"^payment-methods/(?P<pk>\d+)/update/$", pinax_views.PaymentMethodUpdateView.as_view(), name="pinax_stripe_payment_method_update"),
    url(r"^webhook/$", pinax_views.Webhook.as_view(), name="pinax_stripe_webhook"),
    url(
        r"^payment-methods/$",
        RedirectView.as_view(url=reverse_lazy("pinax_stripe_subscription_list"), permanent=True),
        name="pinax_stripe_payment_method_list"
    )
]
