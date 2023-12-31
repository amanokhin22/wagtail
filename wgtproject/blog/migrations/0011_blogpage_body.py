# Generated by Django 4.2.2 on 2023-06-23 09:33

from django.db import migrations
import wagtail.blocks
import wagtail.fields
import wagtail.images.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0010_alter_blogpage_stream'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogpage',
            name='body',
            field=wagtail.fields.StreamField([('gallery', wagtail.blocks.ListBlock(wagtail.images.blocks.ImageChooserBlock())), ('heading', wagtail.blocks.CharBlock(form_classname='title')), ('paragraph', wagtail.blocks.RichTextBlock()), ('image', wagtail.images.blocks.ImageChooserBlock())], blank=True, use_json_field=True),
        ),
    ]
