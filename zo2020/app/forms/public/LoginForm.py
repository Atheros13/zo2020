"""
Definition of forms.
"""

from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.utils.translation import ugettext_lazy as _
from django.core.exceptions import ValidationError

from app.models import User

class PublicLoginForm(AuthenticationForm):
    
    """ """

    username = forms.CharField(max_length=254,
                               widget=forms.TextInput({
                                   'class': 'form-control',
                                   'placeholder': ''}),
                               )
    password = forms.CharField(label=_("Password"),
                               widget=forms.PasswordInput({
                                   'class': 'form-control',
                                   'placeholder':''}))

    def clean(self):

        """Overrides clean(), checks if the password being used is a 
        correct temporary one, if so, it deletes the old password, and makes 
        the password the temporary one. 
        
        This allows a later login check to redirect the user to a 
        change password page. """
        
        user_check = User.objects.filter(email=self.cleaned_data['username'])
        if user_check:
            user = user_check[0]

        # if there is a temporary password...
        if user_check and user.temporary_password != '':

            # check if the one given is that password, in which case, 
            # remove the old password and use the temporary one
            if  self.cleaned_data['password'] == user.temporary_password:
                user.set_password(user.temporary_password)
                user.save()
            # check if the one given is the old password, in which case
            # delete the temporary password and date
            elif user.check_password(self.cleaned_data['password']):
                user.temporary_password = ''
                user.temporary_date = None
                user.save()

        return super(PublicLoginForm, self).clean()