from wagtail.models import Page
from wagtail.fields import RichTextField, StreamField
from wagtail.admin.panels import FieldPanel
from wagtail import blocks
from wagtail.images.blocks import ImageChooserBlock


class HomePage(Page):
    intro = RichTextField(blank=True, null=True)
    body = StreamField([
        ('gallery', blocks.ListBlock(blocks.RichTextBlock(label="news"), default=[])),
        ('heading', blocks.RichTextBlock()),
        ('paragraph', blocks.RichTextBlock()),
        ('image', ImageChooserBlock()),
    ], blank=True, null=True, use_json_field=True)

    content_panels = Page.content_panels + [
        FieldPanel('intro'),
        FieldPanel('body'),
    ]
