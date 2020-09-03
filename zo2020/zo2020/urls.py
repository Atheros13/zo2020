"""
Definition of urls for zo2020.
"""

from datetime import datetime
from django.urls import path, include
from django.contrib import admin
from django.contrib.auth.views import LogoutView as PublicLogoutView

from app.views.public import PublicHomeView, PublicAboutView
from app.views.public import PublicLoginView, PublicSignupView, PublicSignupSentView
from app.views.public import PublicTournamentsView
from app.views.public import PublicContactView, PublicContactSentView

urlpatterns = [
    
    # PUBLIC
    path('', PublicHomeView.as_view(), name='public-home'),
    path('about/', PublicAboutView.as_view(), name='public-about'),
    path('tournaments/', PublicTournamentsView.as_view(), name='public-tournaments'),

    path('contact/', PublicContactView.as_view(), name='public-contact'),
    path('contact/sent/', PublicContactSentView.as_view(), name='public-contact-sent'),

    # SIGNUP, LOGIN/LOGOUT
    path('signup/', PublicSignupView.as_view(), name='public-signup'),
    path('signup/sent/', PublicSignupSentView.as_view(), name='public-signup-sent'),

    path('login/', PublicLoginView.as_view(), name='public-login'),
    path('logout/', PublicLogoutView.as_view(next_page='/'), name='public-logout'),

    path('login/password-request', PublicPasswordRequest.as_view(), name='public-password-request'),

    # ACCOUNT


    # HUB


    # TOURNAMENT


    # ADMIN
    path('admin/', admin.site.urls),
]
