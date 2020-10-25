from __future__ import unicode_literals

from django.db import models

from app.models import Participant

class Competitor(models.Model):

    '''This is the object that competes in a contest '''

    participant = models.OneToOneField(Participant, null=True, related_name='competitor')

    competitors = models.ManyToManyField(Competitor, related_name='teams')
    # > teams
    name = models.CharField(max_length=30, blank=True) # Team Name 

    def __str__(self):

        if self.name == '':

            return self.participant

    def is_team(self):

        """ Returns True if there is more than one Competitors"""

        if self.competitors:
            return True
        return False