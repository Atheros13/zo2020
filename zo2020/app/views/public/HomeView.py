from django.http import HttpRequest
from django.shortcuts import render
from django.views import View

from datetime import datetime

class PublicHomeView(View):

    template_name = 'public/home.html'
    title = 'ZO-Sports'

    def get(self, request, *args, **kwargs):

        return render(
            request,
            self.template_name,
            {
                'title':self.title,
                'year':datetime.now().year,
            }
        )
