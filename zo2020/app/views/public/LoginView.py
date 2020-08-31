from django.http import HttpRequest
from django.shortcuts import render
from django.contrib.auth.views import LoginView

from datetime import datetime

from app.forms.public import PublicLoginForm

class PublicLoginView(LoginView):

    template_name='public/login.html',
    authentication_form=PublicLoginForm,

    def get(self, request, *args, **kwargs):

        return render(
            request,
            self.template_name,
            {
                'title':'Log in',
                'message': 'About page',
                'year':datetime.now().year,
            }
        )
