from django.db import models
from django.db.models import Q
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType

from app.models.tournament.tournament import Tournament
from app.models.tournament.contest import TournamentContest
from app.models.tournament.grade import TournamentGrade

class TournamentEvent(models.Model):
    
    """ """

    tournament = models.ForeignKey(Tournament, on_delete=models.CASCADE, related_name='events')
    event = models.ForeignKey(Event, on_delete=models.CASCADE, related_name='tournaments')
    name = models.CharField(max_length=30, blank=True)

    def __str__(self):

        if self.name == '':
            try:
                contest = self.event.contest
                contest_name = TournamentContest.objects.filter(tournament=self.tournament, 
                                                                contest=contest)[0].__str__()
                grade = self.event.grade
                grade_name = TournamentGrade.objects.filter(tournament=self.tournament,
                                                            grade=grade)[0].__str__()
                return '%s %s' % (grade_name, contest_name)
            except:
                return self.event.__str__()
        return self.name