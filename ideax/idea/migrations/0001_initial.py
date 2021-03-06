# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-06-05 07:20
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Idea',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug_id', models.CharField(max_length=10, unique=True)),
                ('title', models.CharField(blank=True, max_length=256)),
                ('text', models.TextField(blank=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='authored_ideas', to=settings.AUTH_USER_MODEL)),
                ('upvoters', models.ManyToManyField(blank=True, related_name='upvoted_ideas', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
