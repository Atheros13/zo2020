from __future__ import unicode_literals

from django.db import models

from app.models import Grade
from app.models import Tournament

class TournamentGrade(models.Model):

    grade = models.ForeignKey(Grade, on_delete=models.CASCADE, related_name='tournament_grades')
    tournament = models.ForeignKey(Tournament, on_delete=models.CASCADE, related_name='tournament_grades')
    name = models.CharField(max_length=30) # U13 Girls, Under 13 Girls, Under Thirteen Ladies, etc

    def __str__(self):

        return self.name
