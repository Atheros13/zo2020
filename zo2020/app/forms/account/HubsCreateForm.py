from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from django.core.mail import send_mail
from django import forms

from django_countries.fields import CountryField
from django_countries.widgets import CountrySelectWidget

from app.forms.validators import unique_hub_email
from app.models import Hub, HubType, HubAddress

class AccountHubsCreateForm(forms.Form):

    """ """

    name = forms.CharField(label=_("Hub Name"),
                               widget=forms.TextInput({
                                   'class': 'form-control',
                                   'placeholder':''}))
    type = forms.ModelChoiceField(label=_("Hub Type"),
                                  queryset=HubType.objects.all(),
                                          widget=forms.Select({
                                            'class': 'form-control',
                                            'placeholder': ''}),
                                          help_text='What sort of Hub is this? A School or Club, or choose Other and elaborate in description below')
    description = forms.CharField(label=_("Description"),
                               widget=forms.Textarea({
                                   'class': 'form-control',
                                   'placeholder':''}),
                               help_text='Further describe what sort of Hub this is i.e. Catholic Primary School, Kura Kaupapa Y1 - Y8')


    phone = forms.CharField(label=_("Hub Phone Name"),
                               widget=forms.TextInput({
                                   'class': 'form-control',
                                   'placeholder':''}),
                               validators=[],)
    email = forms.EmailField(label=_("Hub Contact Email"),
                             widget=forms.EmailInput({
                                   'class': 'form-control',
                                   'placeholder': ''}),
                             validators=[unique_hub_email],)

    line1 = forms.CharField(label=_("Address Line 1"),
                               widget=forms.TextInput({
                                   'class': 'form-control',
                                   'placeholder':''}))
    line2 = forms.CharField(label=_("Address Line 2"),
                               widget=forms.TextInput({
                                   'class': 'form-control',
                                   'placeholder':''}),
                               required=False)
    suburb =  forms.CharField(label=_("Suburb"),
                               widget=forms.TextInput({
                                   'class': 'form-control',
                                   'placeholder':''}),
                               required=False)
    town_city = forms.CharField(label=_("Town or City"),
                               widget=forms.TextInput({
                                   'class': 'form-control',
                                   'placeholder':''}))
    postcode = forms.CharField(label=_("Postcode"),
                               widget=forms.TextInput({
                                   'class': 'form-control',
                                   'placeholder':''}),
                               required=False)
    country = CountryField().formfield(widget=CountrySelectWidget(
                                        attrs={"class": "form-control"}))

    message = forms.CharField(label=_("Additional Information"),
                               widget=forms.Textarea({
                                   'class': 'form-control',
                                   'placeholder':''}),
                               required=False,
                               help_text='Please add a message and/or any additional information that the ZO-SPORTS team may need to know.')

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None)
        super(AccountHubsCreateForm, self).__init__(*args, **kwargs)
           
    def clean(self):

        """ """

        data = self.cleaned_data

        return super(AccountHubsCreateForm, self).clean()

    def process_form(self, request, *args, **kwargs):

        """Creates linked Hub and HubAddress objs and sets the Hub.is_active 
        to False, then emails the requester and ZO-SPORTS """

        data = self.cleaned_data

        duplicates = self.check_hub_duplicates()

        # create Hub and save
        description = data['description']
        description += '\n-\n' + data['message']
        self.hub = Hub(description=description, name=data['name'],
                       phone=data['phone'], email=data['email'],
                       main_contact=self.user.account,
                       is_active=False)
        self.hub.save()
        self.hub.type=data['type']
        self.hub.admins.add(self.user.account)
        self.hub.save()

        # create and link HubAddress and save
        self.address = HubAddress(hub=self.hub,
                                  line1=data['line1'], line2=data['line2'],
                                  suburb=data['suburb'], town_city=data['town_city'],
                                  postcode=data['postcode'], country=data['country'])
        self.address.save()


        # send email to ZO-Sports - with note about any similar Hubs
        send_mail('ZO-SPORTS - Hub Request', self.message_to_zosports(duplicates), 
                        self.user.email, ['info@zo-sports.com'])


        # send email to User that requested 
        send_mail('ZO-SPORTS - Hub Request Received - %s' % self.hub.id, self.message_to_requester(), 
                        'no-reply@zo-sports.com', [self.user.email])

    def check_hub_duplicates(self):

        """ Returns a queryset of all Hubs that have the same country 
        and town and a similar street. """

        data = self.cleaned_data

        street = None
        for word in [i for i in data['line1'].split() if not i.isdigit()]:
            if len(word) > 3:
                street = word
                break
        
        hubs = Hub.objects.filter(
                    address__country=data['country']).filter(
                        address__town_city=data['town_city']).filter(
                            address__line1__icontains=street)

        return hubs

    def message_to_zosports(self, duplicates):

        hubs = duplicates

        message = 'HUB %s %s\n' % (self.hub.name, self.hub.id)
        message += 'REQUESTED BY: %s %s\n\n' % (self.user.__str__(), self.user.account.id)
        message += 'TYPE: %s\nNOTES: %s\n\n' % (self.hub.type.__str__(),
                                                                  self.hub.description)
        if hubs:
            message += 'POSSIBLE DUPLICATES:\n'
            for hub in hubs:
                message += '%s - %s - %s\n%s\n' % (hub.name, hub.type.__str__(),
                                                   hub.address.line1,
                                                   hub.description)

        message += '\nwww.zo-sports.com/admin/app/hub\n' #/%s' % self.hub.id #unless this is actually the HubAdmin.id
        message += 'www.zo-sports.com/admin/app/hub/%s/change' % self.hub.id

        return message

    def message_to_requester(self):

        message = 'Kia ora %s,\n\n' % self.user.__str__()
        message += 'We have received your request to create %s as a Hub for ZO-SPORTS.\n' % self.cleaned_data['name']
        message += 'You will only receive a confirmation email if this request is accepted, '
        message += 'and it may take up to 72 hours to hear back.\n\n'
        message += 'ZO-SPORTS'

        return message