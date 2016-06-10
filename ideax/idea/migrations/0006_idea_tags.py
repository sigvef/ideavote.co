# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-06-10 11:10
from __future__ import unicode_literals

from django.db import migrations
import taggit.managers


class Migration(migrations.Migration):

    dependencies = [
        ('taggit', '0002_auto_20150616_2121'),
        ('idea', '0005_auto_20160609_2302'),
    ]

    operations = [
        migrations.AddField(
            model_name='idea',
            name='tags',
            field=taggit.managers.TaggableManager(help_text='A comma-separated list of tags.', through='taggit.TaggedItem', to='taggit.Tag', verbose_name='Tags'),
        ),
    ]
