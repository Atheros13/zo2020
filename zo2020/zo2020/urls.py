"""
Definition of urls for zo2020.
"""

from datetime import datetime
from django.urls import path
from django.contrib import admin
from django.contrib.auth.views import LoginView, LogoutView

from app import forms

from app.views import PublicHomeView, PublicAboutView, PublicContactView

urlpatterns = [

    path('', PublicHomeView.as_view(), name='home'),
    path('about/', PublicAboutView.as_view(), name='about'),
    path('contact/', PublicContactView.as_view(), name='contact'),


    path('login/',
         LoginView.as_view
         (
             template_name='public/login.html',
             authentication_form=forms.BootstrapAuthenticationForm,
             extra_context=
             {
                 'title': 'Log in',
                 'year' : datetime.now().year,
             }
         ),
         name='login'),
    path('logout/', LogoutView.as_view(next_page='/'), name='logout'),
    path('admin/', admin.site.urls),
]
