from test_plus.test import TestCase

from {{ cookiecutter.project_slug }}.beta.forms import InviteForm, RequestForm
from {{ cookiecutter.project_slug }}.beta.models import Request

class InviteFormTestCase(TestCase):

    def test_form_valid(self):
        form = InviteForm({'code': "12345678901234567890123456789012345678901234567890"})
        self.assertTrue(form.is_valid())

    def test_form_invalid(self):
        # code too short
        form = InviteForm({'code': "1"})
        self.assertFalse(form.is_valid())

        # code too large
        form = InviteForm({'code': "123456789012345678901234567890123456789012345678901"})
        self.assertFalse(form.is_valid())


class RequestFormTestCase(TestCase):

    def test_form_valid(self):
        form = RequestForm({'email': "foo@bar.com"})
        self.assertTrue(form.is_valid())
        form.save()
        self.assertTrue(Request.objects.filter(email="foo@bar.com").exists())

    def test_form_invalid(self):
        # not using a valid mail
        form = RequestForm({'email': "foo"})
        self.assertFalse(form.is_valid())
