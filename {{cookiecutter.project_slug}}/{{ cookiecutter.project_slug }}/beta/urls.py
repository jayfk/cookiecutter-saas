# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

from django.conf.urls import url

from . import views

urlpatterns = [
    url(
        regex=r'^request-invite/$',
        view=views.RequestInviteView.as_view(),
        name='request-invite'
    ),
    url(
        regex=r'^request-success/$',
        view=views.RequestInviteSuccess.as_view(),
        name='request-success'
    ),
]
