from django.views.generic.edit import FormView

from datetime import datetime

from app.views.generic import GenericContactSentView
from app.forms.public import PublicSignupForm

class PublicSignupView(FormView):

    template_name = 'public/signup.html'
    form_class = PublicSignupForm
    success_url = '/signup/sent'

    ## GET level methods
    def get_context_data(self, **kwargs):

        context = super().get_context_data(**kwargs)

        context['submit_text'] = 'Signup'
        context['title'] = 'Signup'
        context['success_url'] = self.success_url
        context['message'] = 'Signup below'
        context['year'] = datetime.now().year

        return context

    ## POST level methods
    def form_valid(self, form):

        form.process_form(self.request)

        return super().form_valid(form)

class PublicSignupSentView(GenericContactSentView):

    title = 'Signup'
    message = 'A temporary password has been sent to the email you provided. Please check your spam if it doesn\'t arrive in the next 5 minutes'