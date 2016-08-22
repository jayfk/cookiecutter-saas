from test_plus.test import TestCase
from django.core.urlresolvers import reverse

from {{ cookiecutter.project_slug }}.blog.models import Entry


class EntryListViewTestCase(TestCase):

    url = "blog:entries"

    def test_has_title(self):
        resp = self.client.get(reverse(self.url))
        self.assertContains(resp, "<title>Blog</title>")


class EntryViewTestCase(TestCase):

    def test_has_title(self):
        entry = Entry.objects.create(title="the foo title")
        entry.save()
        resp = self.client.get(entry.get_absolute_url())
        self.assertContains(resp, "<title>the foo title</title>")
