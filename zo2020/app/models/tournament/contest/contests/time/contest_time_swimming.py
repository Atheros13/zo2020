from django.db import models

from app.models.abstract.contest.contests import ContestTime

class ContestTimeSwimming(ContestTime):
    
    """ """

    #distance = None
    #style = models.CharField(max_length=20, blank=True)
    


    class Meta:

        abstract = True