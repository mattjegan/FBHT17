# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-29 07:29
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_auto_20170429_0647'),
    ]

    operations = [
        migrations.CreateModel(
            name='CompleteReceipt',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('completed', models.DateTimeField(default=datetime.datetime.now, editable=False)),
                ('mission', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.Mission')),
                ('profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.Profile')),
            ],
        ),
    ]
