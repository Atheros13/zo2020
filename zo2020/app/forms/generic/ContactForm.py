from django.core.mail import send_mail

from django import forms

class GenericContactForm(forms.Form):

    '''Creates a Form object that View will instruct a Template 
    to interpret into a form for people to fill out. The View will 
    use its get() method to create the blank form, and the 
    post() method to access the process_form() method of the Form.
    
    Generic fields are name, email and message (all of which are 
    required).    
    
    '''

    ## CLASS ATTRIBUTES
    contact_type = 'Generic' # needs to be altered when inherited
    to_emails = ['info@zo-sports.com']
    field_order = ['name', 'email', 'message']

    ## FIELDS 
    name = forms.CharField(label='Name', max_length=30, min_length=3)
    email = forms.EmailField(label='Email')
    message = forms.CharField(label='Message', min_length=10, widget=forms.Textarea)

    def process_form(self, request, *args, **kwargs):

        ''' '''

        self.send_email()


    def send_email(self, *args, **kwargs):

        '''Cleans the data and sends a formatted email to the correct
        email at ZO. '''

        data = self.cleaned_data

        subject = 'Contact - %s' % self.contact_type
        message = ''
        for field in self.field_order:
            if field == 'email':
                continue
            message += '%s: %s\n\n' % (field.upper(), data[field]) 
        email = data['email']

        send_mail(subject, message, email, self.to_emails)
