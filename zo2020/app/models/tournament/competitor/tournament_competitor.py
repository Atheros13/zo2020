from __future__ import unicode_literals

from django.db import models

from app.models import Competitor

class TournamentCompetitor(models.Model):

    '''This is the object that competes in a tournament i.e. the House '''

    name = models.CharField(max_length=30, blank=True) # 





    competitors = models.ManyToManyField(Competitor, related_name='tournament_competitors')

