from __future__ import unicode_literals

from django.db import models

class ActivityType(models.Model):

    type = models.CharField(max_length=30, unique=True)
    description = models.TextField(blank=True)

class Activity(models.Model):

    type = models.ForeignKey(ActivityType, on_delete=models.PROTECT, related_name='activities')
    activity = models.CharField(max_length=30)
    sub_activity = models.CharField(max_length=30)
    description = models.TextField(blank=True)
