from django.db import models

from app.models.abstract.contest.contest import Contest

class ContestDistance(Contest):
    
    """ """

    style = models.CharField(max_length=20, blank=True)

    class Meta:

        abstract = True