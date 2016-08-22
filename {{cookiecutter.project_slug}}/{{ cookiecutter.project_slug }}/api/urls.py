# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf.urls import include, url

urlpatterns = [
    url(
        r'^v1/',
        include('{{ cookiecutter.project_slug }}.api.v1.urls', namespace="v1"),
    ),
]
