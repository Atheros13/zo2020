from django import forms

from django_countries.fields import CountryField

class PublicSignupForm(forms.Form):

    ''' '''

    firstname = forms.CharField(max_length=30, min_length=1,
                           widget=forms.TextInput({
                                   'class': 'form-control',
                                   'placeholder': ''}))
    lastname = forms.CharField(max_length=30, min_length=1,
                           widget=forms.TextInput({
                                   'class': 'form-control',
                                   'placeholder': ''}))    
    email = forms.EmailField(widget=forms.EmailInput({
                                   'class': 'form-control',
                                   'placeholder': ''}))
    dob = forms.EmailField(widget=forms.DateInput({
                                   'class': 'form-control',
                                   'placeholder': ''}))
    country = CountryField().formfield()

    ## Template Methods
    def field_list(self):
        
        return []

    ## Process Methods
    def process_form(self, request, *args, **kwargs):

        '''All forms have this method, it can be overwritten to process data
        as required.'''

        pass

    def send_email(self, *args, **kwargs):

        #send_mail(subject, message, email, self.to_emails)

        pass
