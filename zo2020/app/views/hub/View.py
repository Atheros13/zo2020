from django.http import HttpRequest
from django.shortcuts import render
from django.views import View

from datetime import datetime

from app.models import Hub

class HubView(View):

    template_name = 'generic/basic-page.html'

    def get(self, request, *args, **kwargs):

        hub = Hub.objects.filter(id=request.session['hub'])[0]

        return render(
            request,
            self.template_name,
            {
                'title':hub.__str__(),
                'year':datetime.now().year,
            }
        )
