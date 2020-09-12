from __future__ import unicode_literals

from django.db import models

class Gender(models.Model):

    ''' '''

    CHOICES_GENDER = [
        ('Female', 'Female'),
        ('Male', 'Male'),
        ('Non-Binary', 'Non-Binary')
        ]

    gender = models.CharField(max_length=10, choices=CHOICES_GENDER)

    ### META DATA ###

    def __str__(self):

        ''' '''

        return self.gender




