from django import forms

from django_countries.fields import CountryField

from app.models import User, Account, AccountName, AccountAddress
from app.validators import unique_user

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
    dob = forms.EmailField(label='Date of Birth', widget=forms.DateInput({
                                   'class': 'form-control',
                                   'placeholder': 'dd/mm/yy'}))
    country = CountryField().formfield()


    ## Process Methods
    def process_form(self, request, *args, **kwargs):

        ''' '''

        # Create Models
        self.build_account(self.build_user())

        # Send Confirmation/Temporary Password Email
        self.send_email(user)

    def build_user(self):

        user = User(email=self.email)
        user.temporary_password = User.objects.make_random_password()
        user.set_password(user.temporary_password)
        user.save()

        return user

    def build_account(self, user):

        account = Account(user=user, dob=self.dob)
        account.save()

        name = AccountName(account=account,
                            firstname=self.firstname, lastname=self.lastname)
        name.save()
        address = AccountAddress(account=account,
                                 country=self.country)
        address.save()

    def send_email(self, user, *args, **kwargs):

        subject = 'ZO-SPORTS: Signup'
        message = 'Kia ora %s %s\n\n' % (self.firstname, self.lastname)

        message += ''
        message += ''
        message += ''

        email = 'no-reply@zo-sports.com'

        send_mail(subject, message, email, [user.email])