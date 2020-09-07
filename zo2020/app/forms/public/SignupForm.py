from django import forms
from django.core.mail import send_mail

from datetime import datetime

from django_countries.fields import CountryField
from django_countries.widgets import CountrySelectWidget

from app.models import User, Account, AccountName, AccountAddress
from app.custom.validators import unique_user



class PublicSignupForm(forms.Form):

    ''' '''

    firstname = forms.CharField(label='First Name', max_length=30, min_length=1,
                           widget=forms.TextInput({
                                   'class': 'form-control',
                                   'placeholder': ''}))
    lastname = forms.CharField(label='Last Name', max_length=30, min_length=1,
                           widget=forms.TextInput({
                                   'class': 'form-control',
                                   'placeholder': ''}))    
    email = forms.EmailField(widget=forms.EmailInput({
                                   'class': 'form-control',
                                   'placeholder': ''}),
                             validators=[unique_user])
    dob = forms.DateField(label='Date of Birth', 
                          input_formats=[
                              '%d/%m/%Y',
                              '%d/%m/%y'],
                          widget=forms.DateInput({
                                   'class': 'form-control',
                                   'placeholder': 'dd/mm/yy'}))
    country = CountryField().formfield(widget=CountrySelectWidget(
                                        attrs={"class": "form-control"}))

    ## Process Methods
    def process_form(self, request, *args, **kwargs):

        ''' '''

        # Create Models

        user, data = self.build_user(self.cleaned_data)
        self.build_account(user, data)

        # Send Confirmation/Temporary Password Email
        self.send_email(user, data)

    def build_user(self, data):

        user = User(email=data['email'])
        user.temporary_password = User.objects.make_random_password()
        user.temporary_date = datetime.now()
        user.set_password(user.temporary_password)
        user.save()

        return user, data

    def build_account(self, user, data):

        account = Account(user=user, dob=data['dob'], phone='', phone2='')
        account.save()

        name = AccountName(account=account,
                            firstname=data['firstname'], middlenames='', lastname=data['lastname'],
                            preferred_name='')
        name.save()
        address = AccountAddress(account=account, line1='', line2='', suburb='',
                                 town_city='', postcode='',
                                 country=data['country'])
        address.save()

    def send_email(self, user, data, *args, **kwargs):

        subject = 'ZO-SPORTS: Signup'
        message = 'Kia ora %s %s\n\n' % (user.account.name.firstname, user.account.name.lastname)

        message += 'Your ZO-Sports Account has been set up, '
        message += 'please go to www.zo-sports.com/login to log in.\n'
        message += 'The first time you log in you will need to choose a new password, '
        message += 'your temporary password is:\n\n%s (case sensitive)\n\n' % user.temporary_password
        message += 'Welcome to ZO-SPORTS\n\n'
        message += '(If you did not request an Account, just ignore this email and the account will be deleted in 72 hours.)'

        email = 'no-reply@zo-sports.com'

        send_mail(subject, message, email, [user.email])