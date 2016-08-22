from django.contrib import admin

from {{ cookiecutter.project_slug }}.blog.models import Entry

admin.site.register(Entry)
