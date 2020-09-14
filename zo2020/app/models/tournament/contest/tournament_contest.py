from django.db import models
from django.db.models import Q
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType

from app.models.tournament.tournament import Tournament

class TournamentContest(models.Model):
    
    """Links a generic Contest model to a specific Tournament and can assign it a 
    Tournament specific name value i.e. 100m Dash, 100 metre Sprint, 100 metres. If a name 
    is not provided, then the default self.contest.__str__() is used. """

    content_type = models.ForeignKey(ContentType, null=True, on_delete=models.CASCADE, limit_choices_to=Q(model__startswith='contest '))
    object_id = models.PositiveIntegerField()

    tournament = models.ForeignKey(Tournament, on_delete=models.CASCADE, related_name='contests')
    contest = GenericForeignKey('content_type', 'object_id')
    name = models.CharField(max_length=30, blank=True)

    def __str__(self):

        if self.name == '':
            return self.contest.__str__()
        return self.name