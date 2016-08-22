from pinax.stripe.models import Plan
from test_plus.test import TestCase

from django.test import override_settings
from django.core.exceptions import ImproperlyConfigured

from {{ cookiecutter.project_slug }}.payments.plan import get_plans, TrialPlan, FreePlan



class TestGetPlansTestCase(TestCase):

    def test_no_plans_exist(self):
        self.assertEquals(get_plans(), [])

    @override_settings(SAAS_SUBSCRIPTION_TYPE="freemium")
    @override_settings(SAAS_PLANS={})
    def test_freemium_but_free_plan_does_not_exist(self):
        with self.assertRaises(ImproperlyConfigured):
            get_plans(free_plan=True)

    @override_settings(SAAS_PLANS={})
    def test_plan_does_not_exist(self):
        Plan.objects.create(stripe_id="foo", name="foo", amount=20, currency="USD", interval="2", interval_count=1)
        with self.assertRaises(ImproperlyConfigured):
            get_plans()

    @override_settings(SAAS_PLANS={"foo": {}})
    def test_plans(self):
        plan = Plan.objects.create(
            stripe_id="foo",
            name="foo", amount=20, currency="USD", interval="2", interval_count=1)

        plans = get_plans()
        self.assertEquals(len(plans), 1)
        self.assertEquals(plans[0]["plan"], plan)

    @override_settings(SAAS_SUBSCRIPTION_TYPE="freemium")
    @override_settings(SAAS_PLANS={"foo": {}, "free": {}})
    def test_plans_with_free(self):
        plan = Plan.objects.create(
            stripe_id="foo",
            name="foo", amount=20, currency="USD", interval="2", interval_count=1)

        plans = get_plans(free_plan=True)
        self.assertEquals(len(plans), 2)
        self.assertTrue(isinstance(plans[0]["plan"], FreePlan))


class FreePlanTest(TestCase):

    def test_free_plan(self):
        plan = FreePlan()
        self.assertEquals(plan.stripe_id, "free")
        self.assertEquals(plan.name, "Free")
        self.assertEquals(plan.amount, 0)


class TrialPlanTest(TestCase):

    def test_free_plan(self):
        plan = TrialPlan()
        self.assertEquals(plan.stripe_id, "trial")
        self.assertEquals(plan.name, "Trial")
        self.assertEquals(plan.amount, 0)
