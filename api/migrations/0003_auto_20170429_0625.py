# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-29 06:25
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_remove_profile_completed_missions'),
    ]

    operations = [
        migrations.AlterField(
            model_name='result',
            name='completed',
            field=models.DateTimeField(default=datetime.datetime.now, editable=False),
        ),
    ]