from django.db import models

from wagtail.models import Page
from wagtail.fields import RichTextField
from wagtail.admin.panels import FieldPanel


class HomePage(Page):
    body = models.CharField(
        max_length=100,
        blank=True,
        null=True
    )
    subtitle = RichTextField(blank=True)
    subtitle2 = RichTextField(blank=True)
    subtitle3 = RichTextField(blank=True)

    content_panels = Page.content_panels + [
        FieldPanel('body'),
        FieldPanel('subtitle'),
        FieldPanel('subtitle2'),
        FieldPanel('subtitle3'),
    ]
