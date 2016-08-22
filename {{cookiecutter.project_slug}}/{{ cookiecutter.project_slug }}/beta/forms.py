from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from django import forms

from {{ cookiecutter.project_slug }}.beta.models import Request

class InviteForm(forms.Form):

    code = forms.CharField(max_length=50, min_length=50)


class RequestForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(RequestForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.add_input(Submit('submit', 'Submit'))

    class Meta:
        model = Request
        fields = ("email",)
