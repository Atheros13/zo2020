from django.views.generic.edit import FormView

from datetime import datetime

from app.views.generic import GenericContactSentView
from app.forms.public import PublicPasswordRequestForm

class PublicPasswordRequestView(FormView):

    template_name = 'generic/basic-form.html'
    form_class = PublicPasswordRequestForm
    success_url = '/login/password-request/sent/'

    ## GET level methods
    def get_context_data(self, **kwargs):

        context = super().get_context_data(**kwargs)

        context['submit_text'] = 'Request'
        context['title'] = 'Password Request'
        context['success_url'] = self.success_url
        context['message'] = 'If you have forgotten your password, we can send a temporary password for you to sign in on.'
        context['year'] = datetime.now().year

        return context

    ## POST level methods
    def form_valid(self, form):

        form.process_form(self.request)

        return super().form_valid(form)

class PublicPasswordRequestSentView(GenericContactSentView):

    title = 'Password Request Sent'
    message = 'A temporary password has been sent to the email you provided. Please check your spam if it doesn\'t arrive in the next 5 minutes. This temporary password will expire in 72 hours.'