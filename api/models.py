from datetime import datetime, timedelta
from django.db import models

def get_expiry():
    return datetime.now() + timedelta(hours=1)

class Step(models.Model):
    type = models.CharField(max_length=50, blank=False, null=False)
    desc = models.TextField(blank=False, null=False)
    cost = models.FloatField(blank=False, null=False)
    mission = models.ForeignKey('api.Mission', blank=False, null=False)


class Mission(models.Model):
    name = models.CharField(max_length=50, blank=False, null=False)
    lat = models.FloatField(blank=True, null=True),
    long = models.FloatField(blank=True, null=True),
    author = models.ForeignKey('api.Profile')
    desc = models.TextField(blank=False, null=False)
    num_users = models.IntegerField(blank=False, null=False)
    expire = models.DateTimeField(default=get_expiry, null=False)
    active = models.BooleanField(default=True, blank=False, null=False)


class Profile(models.Model):
    email = models.EmailField(blank=False, null=False)
    password = models.CharField(max_length=1000, blank=False, null=False)
    first_name = models.CharField(max_length=50, blank=False, null=False)
    last_name = models.CharField(max_length=50, blank=False, null=False)
    current_mission = models.ForeignKey('api.Mission', null=True)
    amount = models.FloatField(default=0.0, blank=False, null=False)


class Result(models.Model):
    profile = models.ForeignKey('api.Profile')
    step = models.ForeignKey('api.Step')
    content = models.TextField(blank=False, null=False)
    completed = models.DateTimeField(default=datetime.now, editable=False)