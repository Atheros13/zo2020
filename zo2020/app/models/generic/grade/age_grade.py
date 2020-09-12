from __future__ import unicode_literals

from django.db import models

from app.custom import CustomYearlessDateField

class AgeGrade(models.Model):

    ''' An age based filter, if open=True then all ages are included, 
    if under=True, then only ages that are under the date (that year) are included, 
    if under=False, then only ages over (not including) the date (that year) 
    are included in the filter, if under=None then the grade is the age as of datetime.now(). '''

    open = models.NullBooleanField(default=False)
    under = models.NullBooleanField(default=None) # <= or >
    age = models.PositiveIntegerField(null=True, default=None)
    date = CustomYearlessDateField(blank=True)

    def __str__(self):

        if self.open == True:
            return 'Open'
        if under == True:
            return 'Under %s' % self.age
        return 'Over %s' % self.age