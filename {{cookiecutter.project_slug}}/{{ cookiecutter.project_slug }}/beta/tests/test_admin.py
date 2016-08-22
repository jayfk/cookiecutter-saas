from test_plus.test import TestCase
from unittest.mock import patch, Mock

from {{ cookiecutter.project_slug }}.beta.models import Invite, Request
from {{ cookiecutter.project_slug }}.beta.admin import send_invite, cancel_invite

class SendInviteTestCase(TestCase):

    @patch("{{ cookiecutter.project_slug }}.beta.admin.send_mail")
    def test_invite(self, send_mail_mock):
        r = Request.objects.create(email="testuser@example.com")

        send_invite(
            modeladmin=None,
            request=Mock(),
            queryset=[r]
        )

        self.assertTrue(send_mail_mock.called)

    @patch("{{ cookiecutter.project_slug }}.beta.admin.send_mail")
    def test_invite_not_sent_if_already_invited(self, send_mail_mock):
        r = Request.objects.create(email="testuser@example.com")
        # this email has been invited already, create an invite object
        Invite.objects.create(request=r)

        send_invite(
            modeladmin=None,
            request=Mock(),
            queryset=[r]
        )

        self.assertFalse(send_mail_mock.called)


class CancelInviteTestCase(TestCase):

    def test_cancel_invite(self):
        # create an invite and a request object and make sure they get deleted
        req = Request.objects.create(email="testuser@example.com")
        invite = Invite.objects.create(request=req)

        cancel_invite(
            modeladmin=None,
            request=Mock(),
            queryset=[req]
        )

        self.assertFalse(Invite.objects.filter(pk=invite.pk).exists())
