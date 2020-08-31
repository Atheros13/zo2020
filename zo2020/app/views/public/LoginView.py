from django.http import HttpRequest
from django.shortcuts import render
from django.contrib.auth.views import LoginView

from datetime import datetime

from app.forms.public import PublicLoginForm

class PublicLoginView(LoginView):

    template_name='public/login.html'
    authentication_form = PublicLoginForm
    message = 'Enter your email and password to log in.'

    def get_context_data(self, **kwargs):

        context = super().get_context_data(**kwargs)
        context['title'] = 'Log in'
        context['year'] = datetime.now().year
        context['message'] = self.message

        return context

class PublicRedirectLoginView(PublicLoginView):

    message = 'Please log in.'
