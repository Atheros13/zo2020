from __future__ import unicode_literals

from django.db import models

from app.models import Account, Hub
from app.models.tournament.activity.activity import Activity

class Tournament(models.Model):

    created_by = models.ForeignKey(Account, null=True, on_delete=models.SET_NULL, related_name='tournaments')
    created_on = models.DateField()

    parent_tournament = models.ForeignKey("Tournament", null=True, on_delete=models.SET_NULL, related_name='child_tournaments')
    # >> child_tournaments

    activity = models.ForeignKey(Activity, null=True, on_delete=models.SET_NULL, related_name='tournaments')

    title = models.CharField(max_length=50)
    #variation i.e. 2020 part of McEvedy Shield, 2020
    description = models.TextField()

    hubs = models.ManyToManyField(Hub, related_name='tournaments')

    competitor_type = None # i.e. inter-Hub, inter-HubGroup, inter-Participant
    competitor_type_name = models.CharField(max_length=20)

    # >> grades = TournamentGrade
    # >> contests = TournamentContest
    # >> events = TournamentEvents

    def __str__(self):

        return self.title
