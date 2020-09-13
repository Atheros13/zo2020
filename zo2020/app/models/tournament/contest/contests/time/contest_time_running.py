from django.db import models

from app.models.abstract.contest.contests import ContestTime
from app.models.tournament.equipment import Apparatus, Obstacle

class ContestTimeRunning(ContestTime):
    
    """ """

    #distance = None
    #style = models.CharField(max_length=20, blank=True)

    apparatus = models.ForeignKey(Apparatus, null=True, on_delete=models.SET_NULL)
    obstacle = models.ForeignKey(Obstacle, null=True, on_delete=models.SET_NULL)

    class Meta:

        abstract = True