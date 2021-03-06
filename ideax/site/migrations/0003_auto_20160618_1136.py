# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-06-18 11:36
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('site', '0002_auto_20160609_2302'),
    ]

    operations = [
        migrations.AddField(
            model_name='sitesettings',
            name='moderators',
            field=models.ManyToManyField(related_name='moderator_sites', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='sitesettings',
            name='owner',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='owned_sites', to=settings.AUTH_USER_MODEL),
        ),
    ]
