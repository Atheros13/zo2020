from __future__ import unicode_literals

from django.db import models
from django_countries.fields import CountryField

class AbstractAddress(models.Model):

    ''' '''

    line1 = models.CharField(max_length=30, blank=True)
    line2 = models.CharField(max_length=30, blank=True)
    suburb = models.CharField(max_length=30, blank=True)
    town_city = models.CharField(max_length=30, blank=True)
    postcode = models.CharField(max_length=13, blank=True)
    country = CountryField()

    ### META DATA ###
    class Meta:

        abstract = True


