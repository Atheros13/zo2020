from datetime import datetime
from django.urls import path, include

from app.views.account import AccountView, AccountSettingsView
from app.views.account import AccountPasswordView
from app.views.account import AccountTournamentsView
from app.views.account import AccountContactView, AccountContactSentView, AccountHubsOpenView
from app.views.account import AccountHubsWhatView, AccountHubsCreateView, AccountHubsCreateSentView

urls_account = [
    
    path('', AccountView.as_view(), name='account-home'),
    path('settings/', AccountSettingsView.as_view(), name='account-settings'),
    path('password/', AccountPasswordView.as_view(), name='account-password'),

    path('hubs/open', AccountHubsOpenView.as_view(), name='account-hubs-open'),

    path('hubs/what', AccountHubsWhatView.as_view(), name='account-hubs-what'),

    path('hubs/create/', AccountHubsCreateView.as_view(), name='account-hubs-create'),
    path('hubs/create/request-sent', AccountHubsCreateSentView.as_view(), name='account-hubs-request-sent'),

    path('tournaments/', AccountTournamentsView.as_view(), name='account-tournaments'),

    path('contact/', AccountContactView.as_view(), name='account-contact'),
    path('contact/sent/', AccountContactSentView.as_view(), name='account-contact-sent'),

]
