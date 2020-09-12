from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from django import forms

from app.models import Hub

class AccountHubsOpenForm(forms.Form):

    """Creates a form with a single Hub labeled field, with a drop down
    menu of all actviated Hubs that the current user has admin rights for."""

    hub = forms.ModelChoiceField(label=_("Choose Hub"),
                                  queryset=Hub.objects.all(),
                                          widget=forms.Select({
                                            'class': 'form-control',
                                            'placeholder': ''}))

    def __init__(self, user, *args, **kwargs):

        """Alters the hub field queryset to only contain activated Hubs that 
        the current user has admin rights for. """

        self.user = user
        super(AccountHubsOpenForm, self).__init__(*args, **kwargs)
        self.fields['hub'].queryset = Hub.objects.all().filter(
                                            admins=self.user.account).filter(
                                                is_active=True)

    def process_form(self, request, *args, **kwargs):

        """Returns the id for the selected Hub. """
        
        data = self.cleaned_data

        return data['hub'].id
