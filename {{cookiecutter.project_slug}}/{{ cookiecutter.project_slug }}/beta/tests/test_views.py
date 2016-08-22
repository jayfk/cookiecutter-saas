from test_plus.test import TestCase

from django.core.urlresolvers import reverse


class ProfileViewTestCase(TestCase):

    url = "beta:request-invite"

    def test_has_title(self):
        resp = self.client.get(reverse(self.url))
        self.assertContains(resp, "<title>Request Invite</title>")

    def test_post(self):
        resp = self.client.post(reverse(self.url), {"email": "foo@bar.com"})
        self.assertRedirects(resp, reverse("beta:request-success"))
