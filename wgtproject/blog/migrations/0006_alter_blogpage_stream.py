# Generated by Django 4.2.2 on 2023-06-22 11:40

from django.db import migrations
import wagtail.blocks
import wagtail.fields
import wagtail.images.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_alter_blogpage_stream'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogpage',
            name='stream',
            field=wagtail.fields.StreamField([('person', wagtail.blocks.StructBlock([('first_name', wagtail.blocks.CharBlock()), ('surname', wagtail.blocks.CharBlock()), ('photo', wagtail.images.blocks.ImageChooserBlock(required=False)), ('biography', wagtail.blocks.RichTextBlock())])), ('heading', wagtail.blocks.CharBlock(form_classname='title')), ('paragraph', wagtail.blocks.RichTextBlock()), ('image', wagtail.images.blocks.ImageChooserBlock())], blank=True, use_json_field=True),
        ),
    ]
