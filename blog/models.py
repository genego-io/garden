from django.db import models
from wagtail.models import Page

from wagtail.models import Page
from wagtail.fields import RichTextField
from wagtail.admin.panels import FieldPanel
from wagtail.search import index


class BlogIndexPage(Page):
    intro = RichTextField(blank=True)

    content_panels = Page.content_panels + [FieldPanel("intro")]


class BlogPage(Page):
    date = models.DateField("Post date", help_text="post date")
    intro = models.CharField(max_length=250, help_text="short introduction")
    body = RichTextField(blank=True, help_text="text of the post")

    search_fields = Page.search_fields + [
        index.SearchField("intro"),
        index.SearchField("body"),
    ]

    content_panels = Page.content_panels + [
        FieldPanel("date"),
        FieldPanel("intro"),
        FieldPanel("body"),
    ]
