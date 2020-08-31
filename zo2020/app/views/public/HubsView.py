from django.http import HttpRequest
from django.shortcuts import render
from django.views import View

from datetime import datetime

class PublicHubsView(View):

    template_name = 'public/hubs-tournaments.html'
    title = 'Hubs'

    def get(self, request, *args, **kwargs):

        return render(
            request,
            self.template_name,
            {
                'title':self.title,
                'message': 'Hubs page',
                'year':datetime.now().year,
            }
        )
