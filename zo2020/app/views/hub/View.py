from django.http import HttpRequest
from django.shortcuts import render
from django.views import View

from datetime import datetime

class HubView(View):

    template_name = 'generic/basic-page.html'

    def get(self, request, *args, **kwargs):

        return render(
            request,
            self.template_name,
            {
                'title':request.session['hub'],
                'year':datetime.now().year,
            }
        )
