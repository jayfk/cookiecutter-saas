from allauth.utils import build_absolute_uri

from django.views.generic import CreateView, TemplateView
from django.core.mail import mail_admins
from django.core.urlresolvers import reverse

from {{ cookiecutter.project_slug }}.beta.models import Request
from {{ cookiecutter.project_slug }}.beta.forms import RequestForm

class RequestInviteView(CreateView):
    model = Request
    form_class = RequestForm

    def get_success_url(self):
        return reverse("beta:request-success")

    def form_valid(self, form):
        mail_admins(
            subject="Invite requested",
            message="{email} requested an invite to your beta.\n\n"
                    "Manage invites at {admin_url}".format(
                        email=form.cleaned_data["email"],
                        admin_url=build_absolute_uri(None, "/foo")
                    )
        )
        return super(RequestInviteView, self).form_valid(form)


class RequestInviteSuccess(TemplateView):
    template_name = "beta/request_success.html"
