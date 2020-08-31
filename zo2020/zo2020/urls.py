"""
Definition of urls for zo2020.
"""

from datetime import datetime
from django.urls import path, include
from django.contrib import admin
from django.contrib.auth.views import LoginView, LogoutView

from app import forms

from app.views.public import PublicHomeView, PublicAboutView, PublicContactView
from app.views.public import PublicHubsView, PublicTournamentsView, PublicLoginView

urlpatterns = [
    
    # PUBLIC
    path('', PublicHomeView.as_view(), name='public-home'),
    path('about/', PublicAboutView.as_view(), name='public-about'),
    path('hubs/', PublicHubsView.as_view(), name='public-hubs'),
    path('tournaments/', PublicTournamentsView.as_view(), name='public-tournaments'),
    path('contact/', PublicContactView.as_view(), name='public-contact'),

    # LOG IN / OUT
    path('login/', PublicLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(next_page='/'), name='logout'),

    # ACCOUNT


    # HUB


    # TOURNAMENT


    # ADMIN
    path('admin/', admin.site.urls),
]
