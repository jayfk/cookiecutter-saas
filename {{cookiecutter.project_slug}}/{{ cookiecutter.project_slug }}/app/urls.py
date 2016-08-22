# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.conf.urls import url

from {{ cookiecutter.project_slug }}.app import views

urlpatterns = [
    url(
        r'^$',
        views.DashboardView.as_view(),
        name='dashboard'
    ),
]
