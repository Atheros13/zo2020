from __future__ import unicode_literals

from django.db import models

from app.models import Grade
from app.models import Tournament

class TournamentGrade(models.Model):

    """Links a generic Grade model to a specific Tournament and can assign it a 
    Tournament specific name value i.e. U13 Girls, Under 13 Ladies. If a name 
    is not provided, then the default self.grade.__str__() is used. """

    tournament = models.ForeignKey(Tournament, on_delete=models.CASCADE, related_name='grades')
    grade = models.ForeignKey(Grade, on_delete=models.CASCADE, related_name='tournaments')
    name = models.CharField(max_length=30, blank=True)

    def __str__(self):

        if self.name == '':
            return self.grade.__str__()
        return self.name