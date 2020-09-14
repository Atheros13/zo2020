from django.db import models

from app.models.tournament.activity.activity import Activity

class Contest(models.Model):
    
    """ """

    activity = models.ForeignKey(Activity, on_delete=models.PROTECT)

    class Meta:

        abstract = True