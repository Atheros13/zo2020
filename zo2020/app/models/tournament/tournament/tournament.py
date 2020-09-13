from __future__ import unicode_literals

from django.db import models

from app.models import Account, Hub
from app.models.tournament.activity.activity import Activity

class Tournament(models.Model):

    ## CREATION STATS
    created_by = models.ForeignKey(Account, null=True, on_delete=models.SET_NULL, related_name='tournaments')
    created_on = models.DateField()

    ## LINKED TOURNAMENTS
    parent_tournament = models.ForeignKey("Tournament", null=True, on_delete=models.SET_NULL, related_name='child_tournaments')
    # >> child_tournaments

    ## ACTIVITY (can be plural)
    activity = models.ManyToManyField(Activity, related_name='tournaments')

    ## TITLE
    title = models.CharField(max_length=30)
    title_qualifier = models.CharField(max_length=20) # ? could this be a model with attributes like type/value i.e. annual/2020
    title_name = models.CharField(max_length=50)

    description = models.TextField()

    ## ADMIN
    hubs = models.ManyToManyField(Hub, related_name='tournaments')
    admins = models.ManyToManyField(Account, related_name='tournament_admins')

    ## EVENTS (WHAT)
    # >> grades = TournamentGrade
    # >> contests = TournamentContest
    # >> events = TournamentEvents

    ## COMPETITORS (WHO)
    competitor_type = None # i.e. inter-Hub, inter-HubGroup, inter-Participant
    competitor_type_name = models.CharField(max_length=20) # i.e. House


    def __str__(self):

        return self.title
