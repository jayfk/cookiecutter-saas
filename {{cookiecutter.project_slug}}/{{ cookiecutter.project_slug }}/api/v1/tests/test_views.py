import json
from test_plus.test import TestCase
from rest_framework.test import APIClient

from django.test import RequestFactory
from django.core.urlresolvers import reverse

from {{ cookiecutter.project_slug }}.users.models import User


class BaseUserTestCase(TestCase):
    def setUp(self):
        self.user = self.make_user()
        self.factory = RequestFactory()
        self.client = APIClient()

    def login(self):
        super(BaseUserTestCase, self).login(username=self.user.username, password="password")


class CurrentUserViewTestCase(BaseUserTestCase):

    url = "api:v1:user"

    def test_needs_login(self):
        resp = self.client.get(
            reverse(self.url)
        )
        self.assertEqual(resp.status_code, 403)

    def test_get(self):
        self.login()
        resp = self.client.get(reverse(self.url))
        data = json.loads(resp.content.decode('utf-8'))
        self.assertEqual(data["email"], self.user.email)

    def test_put_valid(self):
        self.login()
        resp = self.client.put(reverse(self.url), {"name": "foo"}, format="json")
        self.assertEqual(resp.status_code, 200)
        user = User.objects.get(pk=self.user.pk)
        self.assertEquals(user.name, "foo")

    def test_put_invalid(self):
        self.login()
        resp = self.client.put(reverse(self.url), {})
        self.assertEqual(resp.status_code, 400)
