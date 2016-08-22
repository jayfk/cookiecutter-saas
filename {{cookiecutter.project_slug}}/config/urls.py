# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.contrib import admin
from django.views.generic import TemplateView
from django.views import defaults as default_views
from django.http import HttpResponse

from {{ cookiecutter.project_slug }}.views import PricingView

urlpatterns = [
    url(
        r'^$',
        TemplateView.as_view(template_name='pages/home.html'),
        name='home'
    ),
    url(
        r'^health_check/$',
        lambda r: HttpResponse("ok"),
    ),
    url(
        r'^terms-and-conditions/$',
        TemplateView.as_view(template_name='pages/terms_and_conditions.html'),
        name='terms_and_conditions'
    ),
    url(
        r'^privacy-policy/$',
        TemplateView.as_view(template_name='pages/privacy_policy.html'),
        name='privacy_policy'
    ),
    url(
        r'^pricing/$',
        PricingView.as_view(),
        name='pricing'
    ),
    url(
        r'^features/$',
        TemplateView.as_view(template_name='pages/features.html'),
        name='features'
    ),
    # Django Admin, use {% raw %}{% url 'admin:index' %}{% endraw %}
    url(
        settings.ADMIN_URL,
        include(admin.site.urls)
    ),
    {% if cookiecutter.react == "yes" %}
    url(
        r'^api/',
        include('{{ cookiecutter.project_slug }}.api.urls', namespace="api")
    ),
    {% endif %}
    url(
        r'^auth/',
        include('allauth.urls')
    ),
    {% if cookiecutter.blog == "yes" %}
    url(
        r'^blog/',
        include('{{ cookiecutter.project_slug }}.blog.urls', namespace="blog"),
    ),
    url(r'^tinymce/', include('tinymce.urls')),
    {% endif %}
    url(
        r'^app/',
        include('{{ cookiecutter.project_slug }}.app.urls', namespace="app"),
    ),
    {% if cookiecutter.private_beta == "yes" %}
    url(
        r'^beta/',
        include('{{ cookiecutter.project_slug }}.beta.urls', namespace="beta"),
    ),
    {% endif %}
    url(r'^users/',
        include('{{ cookiecutter.project_slug }}.users.urls', namespace='users')),
    url(r"^payments/", include("{{ cookiecutter.project_slug }}.payments.urls")),


] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    # This allows the error pages to be debugged during development, just visit
    # these url in browser to see how these error pages look like.
    urlpatterns += [
        url(
            r'^400/$',
            default_views.bad_request,
            kwargs={'exception': Exception('Bad Request!')}
        ),
        url(
            r'^403/$',
            default_views.permission_denied,
            kwargs={'exception': Exception('Permission Denied')}
        ),
        url(
            r'^404/$',
            default_views.page_not_found,
            kwargs={'exception': Exception('Page not Found')}
        ),
        url(r'^500/$', default_views.server_error),
    ]
