from __future__ import unicode_literals

from django.db import models

from app.models.user import User
from app.models.abstract import AbstractName, AbstractAddress
from app.models.generic import Gender

class Account(models.Model):

    ''' The ZO website level account/profile model. This is model belongs to the User() and 
    can be linked to Hub or Tournament Profiles. '''

    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='account')

    # name = AccountName
    dob = models.DateField(blank=True, null=True, verbose_name='Date of Birth')
    gender = models.ForeignKey(Gender, on_delete=models.CASCADE, blank=True, null=True, related_name='accounts')

    phone = models.CharField(max_length=20, blank=True, verbose_name='Phone Number')
    phone2 = models.CharField(max_length=20, blank=True, verbose_name='Additional Phone Number')
    # address = AccountAddress

    # hubs_admin = Hub 
    # hubs_main_contact = Hub

    ### META DATA ###

    def __str__(self):

        ''' '''
        return self.name.__str__()

    ### 

    def email(self):

        return self.user.email

class AccountName(AbstractName):

    account = models.OneToOneField(Account, on_delete=models.CASCADE, related_name='name')

class AccountAddress(AbstractAddress):

    account = models.OneToOneField(Account, on_delete=models.CASCADE, related_name='address')