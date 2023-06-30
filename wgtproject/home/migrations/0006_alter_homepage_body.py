# Generated by Django 4.2.2 on 2023-06-30 14:15

from django.db import migrations
import wagtail.blocks
import wagtail.fields
import wagtail.images.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_alter_homepage_body'),
    ]

    operations = [
        migrations.AlterField(
            model_name='homepage',
            name='body',
            field=wagtail.fields.StreamField([('gallery', wagtail.blocks.ListBlock(wagtail.blocks.RichTextBlock(label='news'), default=[])), ('heading', wagtail.blocks.RichTextBlock()), ('paragraph', wagtail.blocks.RichTextBlock()), ('image', wagtail.images.blocks.ImageChooserBlock())], blank=True, null=True, use_json_field=True),
        ),
    ]