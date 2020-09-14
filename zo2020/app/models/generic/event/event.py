from django.db import models
from django.db.models import Q
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType

class Event(models.Model):
    
    """ """

    content_type = models.ForeignKey(ContentType, null=True, on_delete=models.CASCADE, limit_choices_to=Q(model__startswith='contest '))
    object_id = models.PositiveIntegerField()   
    
    contest = GenericForeignKey('content_type', 'object_id')
    grade = models.ForeignKey(Grade, on_delete=models.CASCADE, related_name='events')

    def __str__(self):

        return self.grade.__str__() + " " + self.contest.__str__()