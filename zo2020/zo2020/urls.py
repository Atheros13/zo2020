"""
Definition of urls for zo2020.
"""

from datetime import datetime
from django.urls import path, include
from django.contrib import admin
from django.contrib.auth.views import LogoutView as PublicLogoutView

from app.views.public import PublicHomeView, PublicAboutView, PublicLoginView 
from app.views.public import PublicHubsView, PublicTournamentsView
from app.views.public import PublicContactView, PublicContactSentView

urlpatterns = [
    
    # PUBLIC
    path('', PublicHomeView.as_view(), name='public-home'),
    path('about/', PublicAboutView.as_view(), name='public-about'),
    path('hubs/', PublicHubsView.as_view(), name='public-hubs'),
    path('tournaments/', PublicTournamentsView.as_view(), name='public-tournaments'),

    path('contact/', PublicContactView.as_view(), name='public-contact'),
    path('contact/sent/', PublicContactSentView.as_view(), name='public-contact-success'),

    # LOG IN / LOG OUT
    path('login/', PublicLoginView.as_view(), name='public-login'),
    path('logout/', PublicLogoutView.as_view(next_page='/'), name='public-logout'),

    # ACCOUNT


    # HUB


    # TOURNAMENT


    # ADMIN
    path('admin/', admin.site.urls),
]
