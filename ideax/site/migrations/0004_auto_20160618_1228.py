# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-06-18 12:28
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('site', '0003_auto_20160618_1136'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sitesettings',
            name='site',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='settings', to='sites.Site'),
        ),
    ]
