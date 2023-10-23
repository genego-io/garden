from django.db import models

from wagtail.models import Page

from blog.models import BlogPage


class HomePage(Page):
    def get_context(self, request, **kwargs):
        context = super().get_context(request)
        context['pages'] = BlogPage.objects.all()
        return context
