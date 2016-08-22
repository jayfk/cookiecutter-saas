# -*- coding: utf-8 -*-
from pinax.stripe.models import Plan
from decimal import Decimal

from django.conf import settings
from django.core.exceptions import ImproperlyConfigured

from {{ cookiecutter.project_slug }}.payments.defaults import SAAS_SUBSCRIPTION_TYPE as DEFAULT_SAAS_SUBSCRIPTION_TYPE


def get_plans(free_plan=False):
    plans = []
    saas_plans = getattr(settings, 'SAAS_PLANS', {})
    for plan in Plan.objects.all():
        try:
            plans.append({"plan": plan, "meta": saas_plans[plan.stripe_id]})
        except KeyError:
            raise ImproperlyConfigured(
                "Your stripe plan with the id '{stripe_id}' is not in SAAS_PLANS.\n\n"
                "Make sure to add SAAS_PLANS to config/settings/common.py and add the plan "
                "'{stripe_id}' as a key".format(stripe_id=plan.stripe_id)
            )
    if getattr(settings, "SAAS_SUBSCRIPTION_TYPE", DEFAULT_SAAS_SUBSCRIPTION_TYPE) == 'freemium'\
            and free_plan:
        try:
            plans.append({"plan": FreePlan(), "meta": saas_plans["free"]})
        except KeyError:
            raise ImproperlyConfigured(
                "Your SAAS_SUBSCRIPTION_TYPE is 'freemium', but there is no 'free' plan in "
                "SAAS_PLANS\n\n"
                "Make sure to add SAAS_PLANS to config/settings/common.py and add the plan "
                "'free' as a key"
            )
    return sorted(plans, key=lambda p: p["plan"].amount)


class FreePlan(object):

    def __init__(self):
        self.amount = Decimal('0')
        self.name = "Free"

    @property
    def stripe_id(self):
        return self.name.lower()


class TrialPlan(FreePlan):

    def __init__(self):
        super(TrialPlan, self).__init__()
        self.name = "Trial"
