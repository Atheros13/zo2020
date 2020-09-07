from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from django.core.mail import send_mail
from django import forms

from django.contrib.auth import login

class AccountPasswordForm(forms.Form):

    """ """

    ## CLASS ATTRIBUTES
    to_emails = ['info@zo-sports.com']

    ## FIELDS
    current_password = forms.CharField(label=_("Current Password"),
                               widget=forms.PasswordInput({
                                   'class': 'form-control',
                                   'placeholder':''}))
    new_password = forms.CharField(label=_("New Password"),
                               widget=forms.PasswordInput({
                                   'class': 'form-control',
                                   'placeholder':''}))
    confirm_new_password = forms.CharField(label=_("Confirm New Password"),
                               widget=forms.PasswordInput({
                                   'class': 'form-control',
                                   'placeholder':''}))

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None)
        super(AccountPasswordForm, self).__init__(*args, **kwargs)
           
    def clean(self):

        data = self.cleaned_data

        # check current password
        p = data['current_password']
        if not self.user.check_password(p):
            raise ValidationError(
                    _('Incorrect Current Password'),
                )

        # check new passwords
        p1 = data['new_password']
        p2 = data['confirm_new_password']
        if p1 != p2:
            raise ValidationError(
                    _('New passwords do not match'),
                )

        return super(AccountPasswordForm, self).clean()

    def process_form(self, request, *args, **kwargs):

        '''All forms have this method, it can be overwritten to process data
        as required.'''

        data = self.cleaned_data
        user = request.user
        user.set_password(data['new_password'])
        user.temporary_password = ''
        user.temporary_date = None
        user.save()
        
        # When password is changed it signs the person out, 
        # this relogs them back in. 
        login(request, user)