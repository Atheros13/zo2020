from django.db import models
from django.db.models import Q
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType

from app.models.tournament.tournament.tournament import Tournament

class TournamentContest(models.Model):
    
    """ """

    object_id = models.PositiveIntegerField()
    content_type = models.ForeignKey(ContentType, null=True, on_delete=models.CASCADE, 
    											limit_choices_to=Q(model__startswith='contest type'))

    contest = GenericForeignKey('content_type', 'object_id')


    name = models.CharField(max_length=30, blank=True) # i.e. Decathlon 

    def __str__(self):

        if self.name != '':
            return self.name
        return self.contest.__str__()