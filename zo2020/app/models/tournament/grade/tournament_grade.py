from __future__ import unicode_literals

from django.db import models

from app.models import Grade
from app.models import Tournament

class TournamentGrade(models.Model):


    tournament = models.ForeignKey(Tournament, on_delete=models.CASCADE, related_name='grades')
    grade = models.ForeignKey(Grade, on_delete=models.CASCADE, related_name='tournaments')
    name = models.CharField(max_length=30, blank=True) # U13 Girls, Under 13 Girls, Under Thirteen Ladies, etc

    def __str__(self):

        if self.name == '':
            return self.contest.__str__()
        return self.name