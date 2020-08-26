from __future__ import unicode_literals

from django.db import models

from app.models.user import User
from app.models.abstract import AbstractName, AbstractAddress

class Account(models.Model):

    ''' The ZO website level account/profile model. This is model belongs to the User() and 
    can be linked to Hub or Tournament Profiles. '''

    # name = AccountName
    dob = models.DateField()
    gender = models.ForeignKey(Gender, on_delete=models.CASCADE, related_name='account')

    phone = None
    phone2 = None
    # address = AccountAddress
    email = models.EmailField()
    

    ### META DATA ###

    def __str__(self):

        ''' '''
        return self.name.__str__()


class AccountName(AbstractName):

    account = models.OneToOneField(Account, on_delete=models.DELETE, related_name='name')

class AccountAddress(AbstractAddress):

    account = models.OneToOneField(Account, on_delete=models.DELETE, related_name='address')