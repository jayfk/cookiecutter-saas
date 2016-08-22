from django.conf.urls import include, url

from {{ cookiecutter.project_slug }}.blog import views

urlpatterns = [
    url(
        r'^$',
        views.EntryListView.as_view(),
        name='entries'
    ),
    url(
        r'^(?P<slug>[-\w]+)/$',
        views.EntryView.as_view(),
        name='entry'
    ),
]
