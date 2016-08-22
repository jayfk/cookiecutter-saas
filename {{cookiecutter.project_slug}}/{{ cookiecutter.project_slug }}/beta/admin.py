from allauth.utils import build_absolute_uri

from django.contrib import admin
from django.core.mail import send_mail
from django.conf import settings
from django.template.loader import render_to_string
from django.contrib.sites.shortcuts import get_current_site
from django.core.urlresolvers import reverse

from {{ cookiecutter.project_slug }}.beta.models import Invite, Request


def send_invite(modeladmin, request, queryset):
    for r in queryset:
        if not Invite.objects.filter(request=r).exists():
            Invite.objects.create(request=r)
            context = {
                "site": get_current_site(request).domain,
                "invite_link": build_absolute_uri(
                    None,
                    "{}?invite={}".format(reverse("account_signup"), r.invite.code)
                )
            }
            send_mail(
                "Beta Invite",
                message=render_to_string("beta/email/invite.txt", context=context),
                html_message=render_to_string("beta/email/invite.html", context=context),
                from_email=getattr(settings, "DEFAULT_FROM_EMAIL"),
                recipient_list=[r.email]
            )
send_invite.short_description = "Send Invite"


def cancel_invite(modeladmin, request, queryset):
    for r in queryset:
        Invite.objects.filter(request=r).delete()

cancel_invite.short_description = "Cancel Invite"


class RequestAdmin(admin.ModelAdmin):
    list_display = ("email", "invite")
    actions = [send_invite, cancel_invite]


admin.site.register(Invite)
admin.site.register(Request, RequestAdmin)

