from model_utils.models import TimeStampedModel

from django.db import models
from django.utils.crypto import get_random_string
from django.utils.encoding import python_2_unicode_compatible

def get_code():
    return get_random_string(50)


@python_2_unicode_compatible
class Invite(TimeStampedModel):

    code = models.CharField(max_length=50, default=get_code)
    request = models.OneToOneField("Request")

    def __str__(self):
        return self.code


@python_2_unicode_compatible
class Request(TimeStampedModel):

    email = models.EmailField(unique=True)

    def __str__(self):
        return self.email
