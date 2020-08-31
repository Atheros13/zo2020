from django.http import HttpRequest
from django.shortcuts import render
from django.views import View

from datetime import datetime

class PublicTournamentsView(View):

    template_name = 'public/hubs-tournaments.html'
    title = 'Tournament'

    def get(self, request, *args, **kwargs):

        return render(
            request,
            self.template_name,
            {
                'title':self.title,
                'message': 'Tournament page',
                'year':datetime.now().year,
            }
        )
