# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-06-10 13:35
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('idea', '0006_idea_tags'),
    ]

    operations = [
        migrations.AddField(
            model_name='idea',
            name='archived',
            field=models.BooleanField(default=False),
        ),
    ]
