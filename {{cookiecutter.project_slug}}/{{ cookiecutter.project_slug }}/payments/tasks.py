# -*- coding: utf-8 -*-
from pinax.stripe.models import Subscription
from celery import shared_task
import logging

from django.utils import timezone

logger = logging.getLogger(__name__)


@shared_task
def remove_expired_subscriptions():
    # fetches all subscriptions that ended and where a customer is still attached
    qset = Subscription.objects.filter(ended_at__lte=timezone.now(), cancel_at_period_end=True,
                                       customer__user__isnull=False)
    for sub in qset:
        customer = sub.customer
        user = customer.user

        # remove the user from the customer object
        customer.user = None
        customer.save()
    return qset
