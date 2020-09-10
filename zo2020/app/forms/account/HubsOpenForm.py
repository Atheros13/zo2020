from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from django import forms

from app.models import Hub

class AccountHubsOpenForm(forms.Form):

    """  """

    hub = forms.ModelChoiceField(label=_("Choose Hub"),
                                  queryset=Hub.objects.all(),
                                          widget=forms.Select({
                                            'class': 'form-control',
                                            'placeholder': ''}))

    def __init__(self, user, *args, **kwargs):

        self.user = user
        super(AccountHubsOpenForm, self).__init__(*args, **kwargs)
        self.fields['hub'].queryset = Hub.objects.all().filter(
                                            admins=self.user.account).filter(
                                                is_active=True)
           
    def clean(self):

        """ """
        data = self.cleaned_data

        return super(AccountHubsOpenForm, self).clean()

    def process_form(self, request, *args, **kwargs):

        """ """
        
        data = self.cleaned_data
        print('Here %s' % data['hub'])

        return data['hub']
