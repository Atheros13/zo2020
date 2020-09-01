from django.views.generic.edit import FormView

from datetime import datetime

from app.forms.public import PublicContactForm
from app.views.generic import GenericContactSentView

class PublicContactView(FormView):

    template_name = 'public/contact.html'
    form_class = PublicContactForm
    success_url = '/contact/sent'

    ## GET level methods

    def get_context_data(self, **kwargs):

        context = super().get_context_data(**kwargs)

        context['submit_text'] = 'Send'
        context['title'] = 'Contact'
        context['success_url'] = self.success_url
        context['message'] = 'Send a message'
        context['year'] = datetime.now().year

        return context

    ## POST level methods

    def form_valid(self, form):

        form.process_form(self.request)

        return super().form_valid(form)

class PublicContactSentView(GenericContactSentView):

    pass