# -*- coding: utf-8 -*-
from test_plus.test import TestCase
from unittest.mock import patch, Mock, create_autospec, PropertyMock
from pinax.stripe.models import Customer, Card, Subscription, Plan
import jwt
from stripe.error import StripeError, CardError

from django.test.client import Client
from django.core.urlresolvers import reverse
from django.conf import settings
from django.core.urlresolvers import NoReverseMatch
from django.utils import timezone
from django.test import override_settings


class UserTestCase(TestCase):
    def setUp(self):
        self.user = self.make_user()
        self.other_user = self.make_user(username="other_user")
        self.client = Client()


class SubscriptionListViewTestCase(UserTestCase):
    def test_has_title(self):
        self.login(username=self.user.username, password="password")
        resp = self.client.get(reverse("pinax_stripe_subscription_list"))
        self.assertContains(resp, "<title>Subscription</title>")


class CheckoutViewTestCase(UserTestCase):

    def test_has_title(self):
        self.login(username=self.user.username, password="password")
        resp = self.client.get(reverse("pinax_stripe_subscription_create"))
        self.assertContains(resp, "<title>New Subscription</title>")

    def test_user_with_customer_has_no_access(self):
        self.cust = Customer.objects.create(stripe_id="foo", user=self.user)
        self.login(username=self.user.username, password="password")
        resp = self.client.get(reverse("pinax_stripe_subscription_create"))
        self.assertRedirects(resp, reverse("pinax_stripe_subscription_list"))

    def test_form_invalid(self):
        self.login(username=self.user.username, password="password")
        data = {
             "transactionDetails": "some-foo"
         }
        resp = self.client.post(reverse("pinax_stripe_subscription_create"), data)
        self.assertEqual(resp.status_code, 200)
        self.assertFormError(resp, "form", "transactionDetails", "transaction details could'nt be received")

    @patch("{{ cookiecutter.project_slug }}.payments.views.sync_customer")
    @patch("{{ cookiecutter.project_slug }}.payments.views.StripeCustomer")
    def test_form_valid(self, customer, sync_customer):
        customer.retrieve.return_value = {"id": "some_stripe_id"}
        sync_customer.return_value = True
        transaction_details = {
            "customer_id": "bar"
        }
        encoded = jwt.encode(transaction_details, settings.OCTOBAT_PRIVATE_KEY)
        data = {
            "transactionDetails": encoded.decode("utf-8")
        }
        self.login(username=self.user.username, password="password")
        resp = self.client.post(reverse("pinax_stripe_subscription_create"), data)
        customer.retrieve.assert_called_with("bar")
        cust = Customer.objects.get(user=self.user)
        sync_customer.assert_called_with(cust, {"id": "some_stripe_id"})
        self.assertRedirects(resp, reverse("pinax_stripe_subscription_list"))

    @patch("{{ cookiecutter.project_slug }}.payments.views.sync_customer")
    @patch("{{ cookiecutter.project_slug }}.payments.views.StripeCustomer")
    def test_customer_id_not_set(self, customer, sync_customer):

        transaction_details = {
            "foo": "bar"
        }
        encoded = jwt.encode(transaction_details, settings.OCTOBAT_PRIVATE_KEY)
        data = {
            "transactionDetails": encoded.decode("utf-8")
        }
        self.login(username=self.user.username, password="password")
        resp = self.client.post(reverse("pinax_stripe_subscription_create"), data)
        self.assertFormError(resp, "form", "transactionDetails", "transaction details could'nt be received")
        customer.retrieve.assert_not_called()
        sync_customer.assert_not_called()
        self.assertContains(resp, "Unable to process request. Please contact support")

    @patch("{{ cookiecutter.project_slug }}.payments.views.sync_customer")
    @patch("{{ cookiecutter.project_slug }}.payments.views.StripeCustomer")
    def test_cant_retrieve_customer(self, customer, sync_customer):
        customer.retrieve.side_effect = StripeError()
        transaction_details = {
            "customer_id": "bar"
        }
        encoded = jwt.encode(transaction_details, settings.OCTOBAT_PRIVATE_KEY)
        data = {
            "transactionDetails": encoded.decode("utf-8")
        }
        self.login(username=self.user.username, password="password")
        resp = self.client.post(reverse("pinax_stripe_subscription_create"), data, follow=True)
        customer.retrieve.assert_called_with("bar")
        self.assertRedirects(resp, reverse("pinax_stripe_subscription_list"))
        self.assertContains(resp, "Unable to communicate with stripe")

    @patch("{{ cookiecutter.project_slug }}.payments.views.sync_customer")
    @patch("{{ cookiecutter.project_slug }}.payments.views.StripeCustomer")
    def test_customer_sync_failed(self, customer, sync_customer):
        customer.retrieve.return_value = {"id": "some_stripe_id"}
        sync_customer.side_effect = StripeError()
        transaction_details = {
            "customer_id": "bar"
        }
        encoded = jwt.encode(transaction_details, settings.OCTOBAT_PRIVATE_KEY)
        data = {
            "transactionDetails": encoded.decode("utf-8")
        }
        self.login(username=self.user.username, password="password")
        resp = self.client.post(reverse("pinax_stripe_subscription_create"), data, follow=True)
        customer.retrieve.assert_called_with("bar")
        cust = Customer.objects.get(user=self.user)
        sync_customer.assert_called_with(cust, {"id": "some_stripe_id"})
        self.assertRedirects(resp, reverse("pinax_stripe_subscription_list"))
        self.assertContains(resp, "Unable to communicate with stripe")


class SubscriptionTestCase(UserTestCase):

    def setUp(self):
        super(SubscriptionTestCase, self).setUp()
        self.cust = Customer.objects.create(stripe_id="foo", user=self.user)
        self.card = Card.objects.create(customer=self.cust, address_zip_check="foo", country="de", cvc_check="123",
                                   exp_month=12, exp_year=1990, fingerprint="foo")
        self.plan = Plan.objects.create(amount=1, currency="foo", interval="bar", interval_count=2, name="foo", stripe_id="foo")
        self.sub = Subscription.objects.create(customer=self.cust, quantity=1, plan=self.plan,
                                               start=timezone.now())


class SubscriptionDeleteViewTestCase(SubscriptionTestCase):

    def test_has_title(self):
        self.login(username=self.user.username, password="password")
        resp = self.client.get(reverse("pinax_stripe_subscription_delete", kwargs={"pk": self.sub.pk}))
        self.assertContains(resp, "<title>Cancel Subscription</title>")

    def test_other_user_has_no_get_access(self):
        self.login(username=self.other_user.username, password="password")
        resp = self.client.get(reverse("pinax_stripe_subscription_delete", kwargs={"pk": self.sub.pk}))
        self.assertEqual(resp.status_code, 404)


class SubscriptionUpdateViewTestCase(SubscriptionTestCase):

    @override_settings(SAAS_PLANS={"foo": {}})
    def test_has_title(self):
        self.login(username=self.user.username, password="password")
        resp = self.client.get(reverse("pinax_stripe_subscription_update", kwargs={"pk": self.sub.pk}))
        self.assertContains(resp, "<title>Change Plan</title>")

    @patch("pinax.stripe.views.subscriptions")
    def test_deactivate_exceeding_private_repos_called(self, subscriptions):
        other_plan = Plan.objects.create(amount=1, currency="foo", interval="bar", interval_count=2, name="baz", stripe_id="other")
        self.login(username=self.user.username, password="password")
        resp = self.client.post(
            reverse("pinax_stripe_subscription_update", kwargs={"pk": self.sub.pk}),
            data={"plan": other_plan.pk}
        )


class PaymentMethodCreateViewTestCase(UserTestCase):

    def setUp(self):
        super(PaymentMethodCreateViewTestCase, self).setUp()
        self.cust = Customer.objects.create(stripe_id="foo", user=self.user)
        self.card = Card.objects.create(customer=self.cust, address_zip_check="foo", country="de", cvc_check="123",
                                   exp_month=12, exp_year=1990, fingerprint="foo", stripe_id="old_card")

    def test_has_title(self):
        self.login(username=self.user.username, password="password")
        resp = self.client.get(reverse("pinax_stripe_payment_method_create"))
        self.assertContains(resp, "<title>Change Card</title>")

    def test_user_without_customer_has_no_access(self):
        self.login(username=self.user.username, password="password")
        self.cust.delete()
        resp = self.client.get(reverse("pinax_stripe_payment_method_create"))
        self.assertEqual(resp.status_code, 302)

    @patch("pinax.stripe.models.Customer.stripe_customer")
    @patch("{{ cookiecutter.project_slug }}.payments.views.delete_card")
    @patch("{{ cookiecutter.project_slug }}.payments.views.sync_payment_source_from_stripe_data")
    def test_create_card(self, sync_payment_source_from_stripe_data, delete_card, stripe_customer):

        stripe_customer.sources.create.return_value = "create_card"
        self.login(username=self.user.username, password="password")
        data = {
            "stripeToken": "the_foo"
        }
        resp = self.client.post(reverse("pinax_stripe_payment_method_create"), data)
        delete_card.assert_called_with(self.cust, "old_card")
        stripe_customer.sources.create.assert_called_with(source="the_foo")
        sync_payment_source_from_stripe_data.assert_called_with(self.cust, "create_card")

    @patch("{{ cookiecutter.project_slug }}.payments.views.CustomPaymentMethodCreateView.create_card")
    def test_post_on_error(self, create_card):
        create_card.side_effect = CardError("Bad card", "Param", "CODE")
        self.client.login(username=self.user.username, password="password")
        response = self.client.post(
            reverse("pinax_stripe_payment_method_create"),
            {}
        )
        self.assertEquals(response.status_code, 200)
        self.assertTrue("errors" in response.context_data)


class PaymentMethodeUpdateViewTestCase(UserTestCase):

    def setUp(self):
        super(PaymentMethodeUpdateViewTestCase, self).setUp()
        self.cust = Customer.objects.create(stripe_id="foo", user=self.user)
        self.card = Card.objects.create(customer=self.cust, address_zip_check="foo", country="de", cvc_check="123",
                                   exp_month=12, exp_year=1990, fingerprint="foo")

    def test_has_title(self):
        self.login(username=self.user.username, password="password")
        resp = self.client.get(reverse("pinax_stripe_payment_method_update", kwargs={"pk": self.card.pk}))
        self.assertContains(resp, "<title>Update Card</title>")

    def test_other_users_have_no_access(self):
        self.login(username=self.other_user.username, password="password")
        resp = self.client.get(reverse("pinax_stripe_payment_method_update", kwargs={"pk": self.card.pk}))
        self.assertTrue(resp.status_code in [403, 404])


class RestrictedPinaxViewsTestCase(UserTestCase):
    def test_restrict_list_invoices(self):
        with self.assertRaises(NoReverseMatch):
            self.login(username=self.user.username, password="password")
            resp = self.client.get(reverse("pinax_stripe_invoice_list"))
            self.assertEquals(resp.status_code, 404)

    def test_restrict_payment_method_delete(self):
        with self.assertRaises(NoReverseMatch):
            self.login(username=self.user.username, password="password")
            resp = self.client.get(reverse("pinax_stripe_payment_method_delete", kwargs={"pk": 1}))
            self.assertEqual(resp.status_code, 404)

    def test_restrict_payment_method_list(self):
        self.login(username=self.user.username, password="password")
        resp = self.client.get(reverse("pinax_stripe_payment_method_list"))
        self.assertEqual(resp.status_code, 301)


class PricingViewTestCase(TestCase):

    url = "pricing"

    def test_has_title(self):
        resp = self.client.get(reverse(self.url))
        self.assertContains(resp, "<title>Pricing</title>")

    def test_context_data(self):
        resp = self.client.get(reverse(self.url))
        self.assertTrue("plans" in resp.context_data)
