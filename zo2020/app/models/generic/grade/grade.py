from __future__ import unicode_literals

from django.db import models

from .age_grade import AgeGrade
from app.models.generic.person.gender import Gender
from app.models.generic.rank.rank import Rank

class Grade(models.Model):

    ''' A collection of one or more age, gender and/or rank filters. '''

    age = models.ForeignKey(AgeGrade, null=True, on_delete=models.CASCADE, related_name='grades')   
    gender = models.ManyToManyField(Gender, related_name='grades')
    rank = models.ManyToManyField(Rank, related_name='grades')

    def __str__(self):

        pass