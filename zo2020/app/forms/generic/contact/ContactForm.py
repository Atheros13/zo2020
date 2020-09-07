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
    name = forms.CharField(max_length=30, min_length=3,
                           widget=forms.TextInput({
                                   'class': 'form-control',
                                   'placeholder': ''}))
    email = forms.EmailField(widget=forms.EmailInput({
                                   'class': 'form-control',
                                   'placeholder': ''}))
    message = forms.CharField(min_length=10,
                               widget=forms.Textarea({
                                   'class': 'form-control',
                                   'placeholder': ''}))

    ## Template Methods
    def field_list(self):

        '''Returns a list of tuples of ('field name', field_reference) that 
        can be used in a template to dynamically create fields in a form. '''

        fields = []
        for field_name in self.field_order:
            fields.append((field_name, self[field_name]))
        return fields
           
    ## Process Methods
    def process_form(self, request, *args, **kwargs):

        '''All forms have this method, it can be overwritten to process data
        as required.'''

        self.send_email()

    def send_email(self, *args, **kwargs):

        '''Cleans the data and sends a formatted email to the correct
        email at ZO. '''

        data = self.cleaned_data

        subject = 'ZO-SPORTS %s Contact Form' % self.contact_type
        message = ''
        for field in self.field_order:
            if field == 'email':
                continue
            message += '%s: %s\n\n' % (field.upper(), data[field]) 
        email = data['email']

        send_mail(subject, message, email, self.to_emails)
