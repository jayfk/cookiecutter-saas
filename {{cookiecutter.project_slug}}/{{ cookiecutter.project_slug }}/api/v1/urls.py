from rest_framework import routers
from django.conf.urls import url, include

from {{ cookiecutter.project_slug }}.api.v1 import views

# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
#router.register(r'user', views.CurrentUserView)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'user/', views.CurrentUserView.as_view(), name="user"),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
