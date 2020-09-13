from django.db import models

from app.models.abstract.contest.contests import ContestTime
from app.models.tournament.equipment import Apparatus, Obstacle

class ContestType(models.Model):

    type = models.CharField(max_length=30) #i.e. Running, Bicycling, Swimming

class ContestStyle(models.Model):

    type = models.ForeignKey(ContestType, on_delete=models.SET_NULL, related_name='styles')
    
    #
    #
    #
    #

class ContestTimeFastest(ContestTime):
    
    """ """

    style = models.ForeignKey(ContestStyle, on_delete=models.PROTECT, related_name='time_fastest')
    distance = None    
    
    description = models.TextField()
    rules = models.FilePathField()

    # Equipment
    apparatus = models.ForeignKey(Apparatus, null=True, on_delete=models.SET_NULL)
    obstacle = models.ForeignKey(Obstacle, null=True, on_delete=models.SET_NULL)

    class Meta:

        abstract = True