# -*- coding: utf-8 -*-
from rest_framework import serializers

from {{ cookiecutter.project_slug }}.users.models import User


class UserSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = User

        fields = (
            'email', 'name', 'is_on_trial_plan', 'is_on_free_plan', 'is_on_paid_plan',
            'is_customer', 'trial_ends', 'is_trial_active', 'plan_meta', 'card', 'invoices',
            'subscription'
        )

