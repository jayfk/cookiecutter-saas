from django.views.generic import TemplateView

from {{ cookiecutter.project_slug }}.payments.plan import get_plans


class PricingView(TemplateView):

    template_name = "pages/pricing.html"

    def get_context_data(self, **kwargs):
        data = super(PricingView, self).get_context_data(**kwargs)
        data["plans"] = get_plans(free_plan=True)
        data["col"] = "col-md-{}".format(int(12 / len(data["plans"]))) if len(data["plans"]) else "col-md-4"
        return data
