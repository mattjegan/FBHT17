# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-29 05:12
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mission',
            name='expire',
            field=models.DateTimeField(default=datetime.datetime(2017, 4, 29, 6, 12, 24, 584335)),
        ),
    ]