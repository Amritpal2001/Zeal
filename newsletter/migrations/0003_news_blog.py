# Generated by Django 3.1 on 2020-08-22 07:47

from django.db import migrations
import django.utils.timezone
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('newsletter', '0002_news'),
    ]

    operations = [
        migrations.AddField(
            model_name='news',
            name='blog',
            field=tinymce.models.HTMLField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]