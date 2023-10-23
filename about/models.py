from django.db import models
from taggit.models import TaggedItemBase
from wagtail.models import Page
from wagtail.models import Page
from wagtail.fields import RichTextField
from wagtail.admin.panels import FieldPanel, MultiFieldPanel
from wagtail.search import index
from wagtail.models import Page, Orderable


class AboutIndexPage(Page):
    intro = RichTextField(blank=True)
    content_panels = Page.content_panels + [FieldPanel("intro")]

    def get_context(self, request, **kwargs):
        context = super().get_context(request)
        context['aboutpages'] = AboutPage.objects.all()
        return context


class AboutPage(Page):
    date = models.DateField("Post date", help_text="article date")
    intro = models.CharField(max_length=250, help_text="short introduction")
    body = RichTextField(blank=True, help_text="text of the article")

    search_fields = Page.search_fields + [
        index.SearchField("intro"),
        index.SearchField("body"),
    ]

    content_panels = Page.content_panels + [
        MultiFieldPanel([
            FieldPanel('date'),
        ], heading="Article information"),
        FieldPanel('intro'),
        FieldPanel('body'),
    ]
