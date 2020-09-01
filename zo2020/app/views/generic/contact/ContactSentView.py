from django.http import HttpRequest
from django.shortcuts import render
from django.views import View

from datetime import datetime

class GenericContactSentView(View):

    template_name = 'generic/contact/sent.html'
    title = 'Message Sent'
    message = 'Your message has been sent to ZO-SPORTS.'
    next_url_name = 'public-home'    

    def get(self, request, *args, **kwargs):

        return render(
            request,
            self.template_name,
            {
                'title':self.title,
                'message':self.message,
                'next_url_name':self.next_url_name,
                'year':datetime.now().year,
            }
        )
