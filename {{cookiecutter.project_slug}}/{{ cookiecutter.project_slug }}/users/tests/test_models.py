from datetime import timedelta
from pinax.stripe.models import Plan, Customer, Subscription, Card, Invoice
from test_plus.test import TestCase
from unittest.mock import patch, Mock, PropertyMock

from django.utils import timezone
from django.test import override_settings

from {{ cookiecutter.project_slug }}.payments.plan import FreePlan, TrialPlan
from {{ cookiecutter.project_slug }}.payments.defaults import SAAS_SUBSCRIPTION_TYPE, SAAS_TRIAL_LENGTH

class TestUser(TestCase):

    def setUp(self):
        self.user = self.make_user()
        self.customer = Customer.objects.create(user=self.user)
        self.basic_plan = Plan.objects.create(
            stripe_id="basic",
            amount=0,
            currency="EUR",
            interval="foo",
            interval_count=1,
            name="basic"
        )

    def subscribe_to_plan(self, plan):
        return Subscription.objects.create(
            customer=self.customer,
            plan=plan,
            quantity=1,
            start=timezone.now(),
            status="active",
        )

    def test__str__(self):
        self.assertEqual(
            self.user.__str__(),
            "testuser@example.com"  # This is the default username for self.make_user()
        )

    def test_subscription_subscription_does_not_exist(self):
        self.assertEqual(self.user.subscription, None)

    def test_subscription_customer_does_not_exist(self):
        self.customer.delete()
        self.assertEqual(self.user.subscription, None)

    def test_subscription(self):
        sub = self.subscribe_to_plan(self.basic_plan)
        self.assertEqual(self.user.subscription, sub)

    @override_settings(SAAS_SUBSCRIPTION_TYPE='freemium')
    def test_plan_free(self):
        self.assertTrue(isinstance(self.user.plan, FreePlan))

    def test_plan_basic(self):
        self.subscribe_to_plan(self.basic_plan)
        self.assertEqual(self.user.plan, self.basic_plan)

    @override_settings(SAAS_SUBSCRIPTION_TYPE=None)
    def test_is_on_trial(self):
        self.assertFalse(self.user.is_on_trial_plan)
        with patch('{{ cookiecutter.project_slug }}.users.models.User.plan', new_callable=PropertyMock) as mocked_plan:
            mocked_plan.return_value = TrialPlan()
            self.assertTrue(self.user.is_on_trial_plan)

    @override_settings(SAAS_SUBSCRIPTION_TYPE=None)
    def test_is_on_free(self):
        self.assertFalse(self.user.is_on_free_plan)
        with patch('{{ cookiecutter.project_slug }}.users.models.User.plan', new_callable=PropertyMock) as mocked_plan:
            mocked_plan.return_value = FreePlan()
            self.assertTrue(self.user.is_on_free_plan)

    @override_settings(SAAS_SUBSCRIPTION_TYPE=None)
    def test_is_on_paid_plan(self):
        self.assertFalse(self.user.is_on_paid_plan)
        with patch('{{ cookiecutter.project_slug }}.users.models.User.plan', new_callable=PropertyMock) as mocked_plan:
            mocked_plan.return_value = TrialPlan()
            self.assertTrue(self.user.is_on_trial_plan)

    @override_settings(SAAS_SUBSCRIPTION_TYPE="trial")
    def test_trial_ends(self):
        self.assertTrue(self.user.is_on_trial_plan)
        now = timezone.now()
        self.user.date_joined = now
        self.assertEqual(self.user.trial_ends, now + SAAS_TRIAL_LENGTH)

    @override_settings(SAAS_SUBSCRIPTION_TYPE="trial")
    def test_trial_ends(self):
        self.assertTrue(self.user.is_on_trial_plan)
        now = timezone.now()
        self.user.date_joined = now
        self.assertTrue(self.user.is_trial_active)

        self.assertTrue(self.user.is_on_trial_plan)
        self.user.date_joined = now - SAAS_TRIAL_LENGTH - timedelta(days=1)
        self.assertFalse(self.user.is_trial_active)

    def test_invoices_empty(self):
        self.assertEqual(len(self.user.invoices), 0)

    def test_invoices_customer_does_not_exist(self):
        self.customer.delete()
        self.assertEqual(len(self.user.invoices), 0)

    def test_invoices(self):
        invoice = Invoice.objects.create(
            customer=self.customer,
            amount_due=0,
            period_end=timezone.now(),
            period_start=timezone.now(),
            date=timezone.now(),
            subtotal=0,
            total=0
        )
        invoices = self.user.invoices
        self.assertEqual(len(invoices), 1)
        self.assertEqual(invoices[0], invoice)

    def test_is_customer(self):
        self.assertTrue(self.user.is_customer)

    def test_card_customer_doesnt_exist(self):
        self.customer.delete()
        self.assertEqual(self.user.card, None)

    def test_card_card_does_not_exist(self):
        self.assertEqual(self.user.card, None)

    def test_card_success(self):
        the_card = Card.objects.create(
            customer=self.customer,
            exp_month=12,
            exp_year=1777,
        )
        self.assertEqual(self.user.card, the_card)
