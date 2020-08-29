from django.http import HttpRequest
from django.shortcuts import render
from django.views import View

from datetime import datetime

class PublicContactView(View):

    template_name = 'public/contact.html'
    title = 'Contact'

    def get(self, request, *args, **kwargs):

        return render(
            request,
            self.template_name,
            {
                'title':self.title,
                'message': 'Contact page',
                'year':datetime.now().year,
            }
        )
