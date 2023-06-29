from django.db import models
from wagtail.embeds.blocks import EmbedBlock

from wagtail.models import Page
from wagtail.fields import StreamField
from wagtail import blocks
from wagtail.fields import RichTextField
from wagtail.admin.panels import FieldPanel
from wagtail.images.blocks import ImageChooserBlock
import datetime


class PersonBlock(blocks.StructBlock):
    first_name = blocks.CharBlock()
    surname = blocks.CharBlock()
    photo = ImageChooserBlock(required=False)
    biography = blocks.RichTextBlock()

    class Meta:
        template = 'wgtproject/blocks/person.html'
        icon = 'user'


class EventBlock(blocks.StructBlock):
    title = blocks.CharBlock()
    date = blocks.DateBlock()

    def get_context(self, value, parent_context=None):
        context = super().get_context(value, parent_context=parent_context)
        context['is_happening_today'] = (value['date'] == datetime.date.today())
        return context

    class Meta:
        template = 'wgtproject/blocks/event.html'


class BlogIndexPage(Page):
    intro = RichTextField(blank=True)

    def get_context(self, request):
        # Update context to include only published posts, ordered by reverse-chron
        context = super().get_context(request)
        blogpages = self.get_children().live().order_by('-first_published_at')
        context['blogpages'] = blogpages
        return context

    content_panels = Page.content_panels + [
        FieldPanel('intro')
    ]

    class BlogPage(Page):
        author = models.CharField(
            max_length=255,
            blank=True,
            null=True
        )
        date = models.DateField("Post date")
        stream = StreamField([
            ('person', PersonBlock()),
            ('heading', blocks.CharBlock(form_classname="title")),
            ('paragraph', blocks.RichTextBlock()),
            ('image', ImageChooserBlock()),
        ], blank=True, use_json_field=True)

        body = StreamField([
            ('gallery', blocks.ListBlock(ImageChooserBlock())),
            ('heading', blocks.CharBlock(form_classname="title")),
            ('paragraph', blocks.RichTextBlock()),
            ('image', ImageChooserBlock()),
        ], min_num=2, max_num=5, blank=True, use_json_field=True)

        carousel = StreamField([
            ('carousel', blocks.StreamBlock([
                ('image', ImageChooserBlock()),
                ('video', EmbedBlock()),
            ])),
            ('heading', blocks.CharBlock(form_classname="title")),
            ('paragraph', blocks.RichTextBlock()),
            ('image', ImageChooserBlock()),
        ], block_counts={
            'heading': {'min_num': 1, 'max_num': 3},
        }, blank=True, use_json_field=True)

        content_panels = Page.content_panels + [
            FieldPanel('author'),
            FieldPanel('date'),
            FieldPanel('stream'),
            FieldPanel('body'),
            FieldPanel('carousel')
        ]
