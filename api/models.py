from datetime import datetime, timedelta

from django.contrib.auth.models import User
from django.db import models

class Step(models.Model):
    type = models.CharField(max_length=50, blank=False, null=False)
    desc = models.TextField(blank=False, null=False)
    cost = models.FloatField(blank=False, null=False)


class Mission(models.Model):
    name = models.CharField(max_length=50, blank=False, null=False)
    lat = models.FloatField(blank=True, null=True),
    long = models.FloatField(blank=True, null=True),
    author = models.ForeignKey('api.Profile')
    desc = models.TextField(blank=False, null=False)
    # TODO: Calculate cost on serializer
    num_users = models.IntegerField(blank=False, null=False)
    expire = models.DateTimeField(default=datetime.now() + timedelta(hours=1), null=False)
    active = models.BooleanField(default=True, blank=False, null=False)


class Profile(models.Model):
    user = models.ForeignKey(User)
    first_name = models.CharField(max_length=50, blank=False, null=False)
    last_name = models.CharField(max_length=50, blank=False, null=False)
    current_mission = models.ForeignKey('api.Mission', null=True)
    completed_missions = models.ManyToManyField('api.Mission', related_name='completed_missions')
    # TODO: Calculate expired_missions and active_missions on serializer
    amount = models.FloatField(default=0.0, blank=False, null=False)


class Result(models.Model):
    user = models.ForeignKey(User)
    step = models.ForeignKey('api.Step')
    content = models.TextField(blank=False, null=False)
    completed = models.DateTimeField(auto_created=True, editable=False)