# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-29 06:13
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='completed_missions',
        ),
    ]