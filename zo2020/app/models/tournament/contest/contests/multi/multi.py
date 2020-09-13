from django.db import models
from django.db.models import Q
from django.contrib.contenttypes.fields import GenericForeignKey, GenericRelation
from django.contrib.contenttypes.models import ContentType

from app.models.abstract.contest import Contest

class ContestWrapper(models.Model):

    """ """

    object_id = models.PositiveIntegerField()
    content_type = models.ForeignKey(ContentType, null=True, on_delete=models.CASCADE, 
    											limit_choices_to=Q(model__startswith='contest '))

    contest = GenericForeignKey('content_type', 'object_id')


class ContestMulti(Contest):

    """ """

    contests = models.ManyToManyField(ContestWrapper, related_name='multis')

    def __str__(self):

        ''' Returns biathlon, decathlon etc, depending on the number of Contests. '''

        prefix = [None, None, 'bi', 'tri', 'quadr', 'pent', 'hex', 'hept', 'oct', None, 'dec']
        contest_num = len(self.contests)

        if prefix[contest_num] != None:
            return '%sathlon' % prefix[contest_num]
        elif contest_num <= 1:
            return 'Error: %s contest' % contest_num
        return '%s Contests' % contest_num
