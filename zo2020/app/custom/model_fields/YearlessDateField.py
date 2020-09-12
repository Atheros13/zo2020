"""
CustomYearlessDateField is... 


"""
from django.db import models
from django.forms.widgets import MultiWidget, NumberInput, Select
from django import forms
from django.core.validators import ValidationError

import calendar

from app.custom.classes import CustomYearlessDate

class YearlessDateSelect(MultiWidget):

    DAY_CHOICES = tuple([('', '---------' )] + [(i,i) for i in range(1,32)])
    MONTH_CHOICES = tuple([('', '---------' )] + [(i, calendar.month_name[i]) for i in range(1,13)])

    def __init__(self, *args, **kwargs):

        widgets = (
            Select(attrs={'class': 'select-dateinyear-day'}, choices=self.DAY_CHOICES),
            Select(attrs={'class': 'select-dateinyear-month'}, choices=self.MONTH_CHOICES)      
            )

        super(YearlessDateSelect, self).__init__(widgets=widgets, *args, **kwargs)

    def decompress(self, value):

        '''Converts incoming data into formats that the Day/Month Select widgets can take.'''

        if value is None:
            return [None, None]
        return [value.day, value.month]

class YearlessDateFormField(forms.Field):

    widget = YearlessDateSelect

    def clean(self, value):
        if value == ['', '']:
            #If the values are both None, trigger the default validation for null
            super(YearlessDateFormField, self).clean(None)
        else:
            try:
                return CustomYearlessDate(*value)
            except:
                raise ValidationError('Invalid date.')

#

class CustomYearlessDateField(models.Field):

    '''

    '''

    description = "A date without a year, for use in things like birthdays"

    def __init__(self, *args, **kwargs):
        kwargs['max_length'] = 5
        super(CustomYearlessDateField, self).__init__(*args, **kwargs)

    def to_python(self, value):

        print('python %s' % value)

        if isinstance(value, CustomYearlessDate):
            return value
        if not value:
            return None

        # value from db will be eg '01-10'
        return CustomYearlessDate(*value.split('-'))

    def from_db_value(self, value, expression, connection):
        
        return self.to_python(value)

    def get_prep_value(self, value):
        "The reverse of to_python, for inserting into the database"

        print('get prep - %s' % value)

        if value is not None:
            return '%s-%s' % (value.day, value.month)

    def db_type(self, connection):

        return 'char(5)'

    def get_internal_type(self):

        return 'CharField'
    
    def formfield(self, **kwargs):
        # This is a fairly standard way to set up some defaults
        # while letting the caller override them.
        defaults = {'form_class': YearlessDateFormField}
        defaults.update(kwargs)
        return super(CustomYearlessDateField, self).formfield(**defaults)