from django.core.mail import send_mail
from django import forms

class AccountContactForm(forms.Form):

    """ """

    CHOICES_SUBJECT = [
        ('General', 'General'),
        ('Suggestion', 'Suggestion'),
        ('Technical', 'Technical'),    
        ]

    ## CLASS ATTRIBUTES
    contact_type = 'Account' 
    to_emails = ['info@zo-sports.com']
    field_order = ['subject','message']

    ## FIELDS 
    subject = forms.ChoiceField(choices=CHOICES_SUBJECT,
                               widget=forms.Select({
                                   'class': 'form-control',
                                   'placeholder': ''}),
                               )
    message = forms.CharField(min_length=10,
                               widget=forms.Textarea({
                                   'class': 'form-control',
                                   'placeholder': ''}))

    ## Template Methods
    def field_list(self):

        '''Redundant (at the moment)

        Returns a list of tuples of ('field name', field_reference) that 
        can be used in a template to dynamically create fields in a form. '''

        fields = []
        for field_name in self.field_order:
            fields.append((field_name, self[field_name]))
        return fields
           
    ## Process Methods
    def process_form(self, request, *args, **kwargs):

        '''All forms have this method, it can be overwritten to process data
        as required.'''

        self.send_email(request)

    def send_email(self, request, *args, **kwargs):

        '''Cleans the data and sends a formatted email to the correct
        email at ZO. '''

        user = request.user
        data = self.cleaned_data

        subject = 'ZO-SPORTS %s Contact RE: %s' % (self.contact_type, data['subject'])
        message = 'User ID: %s - %s\n\n' % (user.id, user.__str__())
        message += data['message']

        email = user.email

        send_mail(subject, message, email, self.to_emails)
