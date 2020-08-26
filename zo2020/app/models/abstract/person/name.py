from __future__ import unicode_literals

from django.db import models

class AbstractName(models.Model):

    ''' '''

    firstname = models.CharField(max_length=50)
    middlenames = models.CharField(max_length=100, blank=True)
    lastname = models.CharField(max_length=50)

    preferred_name = models.CharField(max_length=50, blank=True)

    ### META DATA ###
    class Meta:

        abstract = True

    def __str__(self):

        ''' '''

        if self.preferred_name == '':
            return self.firstname
        return self.preferred_name

    ### FUNCTIONS ###

    def full_name(self):

        return "%s %s" % (self.__str__(), self.lastname)






