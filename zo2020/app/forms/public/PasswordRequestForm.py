from django import forms
from django.core.mail import send_mail

from datetime import datetime

from app.forms.validators import is_user
from app.models import User

class PublicPasswordRequestForm(forms.Form):

    ''' '''

    email = forms.EmailField(widget=forms.EmailInput({
                                   'class': 'form-control',
                                   'placeholder': ''}),
                             validators=[is_user])

    ## Process Methods
    def process_form(self, request, *args, **kwargs):

        ''' '''

        data = self.cleaned_data

        self.send_email(data)

    def send_email(self, data, *args, **kwargs):

        to_email = data['email']
        user = User.objects.filter(email=to_email)[0]
        
        # creates a temporary password, but does not override it
        user.temporary_password = User.objects.make_random_password()
        user.temporary_date = datetime.now()
        user.save()

        email = 'no-reply@zo-sports.com'
        subject = 'ZO-SPORTS: Password Request'

        message = 'Kia ora %s,\n\n' % user.account.name
        message += 'A new password has been requested for your account.\n'
        message += 'Your temporary password is:\n\n%s (case sensitive)\n\n' % user.temporary_password
        message += 'If you sign in, you will need to change this password. '
        message += 'The temporary password will expire in 72 hours, or if you sign in with the current password. '
        message += 'If you did not request this password, just ignore this email and sign in as usual.\n\n'
        message += 'ZO-SPORTS\n\n'

        send_mail(subject, message, email, [to_email])