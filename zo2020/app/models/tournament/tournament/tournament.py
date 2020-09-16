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
    activity = models.ManyToManyField(Activity, related_name='tournaments') # i.e. Athletics, Atheltics-Track, Athletics-Field

    ## TITLE (this might need to stay like this for the website v1)
    title = models.CharField(max_length=30) 
    title_qualifier = models.CharField(max_length=20, blank=True) 
    title_name = models.CharField(max_length=50, blank=True)

    description = models.TextField()

    ## COMPETITORS (WHO)
    competitor_type = None # i.e. inter-Hub, inter-HubGroup, inter-Participant
    competitor_type_name = models.CharField(max_length=20) # i.e. House
    # >> competitors

    ## EVENTS (WHAT)
    # >> grades = TournamentGrade
    # >> contests = TournamentContest
    # >> events = TournamentEvents

    ## ADMIN
    hubs = models.ManyToManyField(Hub, related_name='tournaments')
    admins = models.ManyToManyField(Account, related_name='tournament_admins')

    def __str__(self):

        if self.title_name == '':
            if self.title_qualifier == '':
                return self.title
            return '%s %s' % (self.title, self.title_qualifier)
        return self.title_name
