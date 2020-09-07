from __future__ import unicode_literals

from django.db import models
from django.core.mail import send_mail

from app.models.account import Account
from app.models.abstract import AbstractAddress

class HubType(models.Model):
    
    """Represent what sort of Hub this is, I can create my own ones and 
    then have them selected. 
    
    Can be Null in Hub to start off with. """

    # hubs = Hub
    type = models.CharField(max_length=30)

    def __str__(self):
        return self.type

class Hub(models.Model):

    """ """
    is_active = models.BooleanField(default=False)

    hub_type = models.ForeignKey(HubType, on_delete=models.SET_NULL, null=True, related_name='hubs')
    description = models.TextField(blank=True)

    name = models.CharField(max_length=50)

    # address = HubAddress
    phone = models.CharField(max_length=20, blank=True, verbose_name='Phone Number')
    email = models.EmailField(unique=True)

    main_contact = models.ForeignKey(Account, null=True, on_delete=models.SET_NULL, related_name='hubs_main_contact')

    # NB: main contact will also be in admins 
    admins = models.ManyToManyField(Account, related_name='hubs_admin')

    # tournaments = Tournament

    def __str__(self):

        return self.name

    ## ADMIN ##

    def send_activation_email(self):

        """Sends an email to the Main Contact, advising that the 
        Hub is now active and that they can access from the 
        Hubs menu when they sign in. """

        subject = 'ZO-SPORTS - Hub Request Accepted'
        message = 'Kia ora %s,\n\n' % self.main_contact
        message += 'Your request for the %s Hub has been accepted.\n' % self.name

        message += 'You can access this Hub through the Hubs menu when you sign in, and this is '
        message += 'where you can add or edit any of the Hub settings. '
        message += 'This is also where you can give other people Admin permission '
        message += 'for the Hub. You have been set up as the Main Contact for %s, ' % self.name
        message += 'This can also be changed in the Hub settings.\n\n'
        message += 'If you have any questions or want to contact ZO-SPORTS about a Hub '
        message += 'issue, please use the Hub contact form.\n\n'
        message += 'ZO-SPORTS'

        send_mail(subject, message, 'no-reply@zo-sports.com', [self.main_contact.user.email])

class HubAddress(AbstractAddress):

    hub = models.OneToOneField(Hub, on_delete=models.CASCADE, related_name='address')