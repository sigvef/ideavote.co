# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-06-09 17:01
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('idea', '0002_auto_20160608_1835'),
    ]

    operations = [
        migrations.AddField(
            model_name='idea',
            name='comment_count',
            field=models.IntegerField(default=0),
        ),
    ]
