from test_plus.test import TestCase

from django.test import RequestFactory
from django.core.urlresolvers import reverse

class BaseUserTestCase(TestCase):
    def setUp(self):
        self.user = self.make_user()
        self.factory = RequestFactory()

    def login(self):
        super(BaseUserTestCase, self).login(username=self.user.username, password="password")


class ProfileViewTestCase(BaseUserTestCase):

    url = "users:update"

    def test_needs_login(self):
        resp = self.client.get(
            reverse(self.url)
        )
        self.assertEqual(resp.status_code, 302)

    def test_has_title(self):
        self.login()
        resp = self.client.get(reverse(self.url))
        self.assertContains(resp, "<title>Profile</title>")

    def test_post(self):
        self.login()
        resp = self.client.post(reverse(self.url), {"name": "foo"})
        self.assertRedirects(resp, reverse(self.url))
