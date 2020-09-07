from django.http import HttpRequest
from django.shortcuts import render

from django.views.generic.edit import FormView

from datetime import datetime

from app.forms.account import AccountPasswordForm

class AccountPasswordView(FormView):

    template_name = 'generic/basic-form.html'
    form_class = AccountPasswordForm
    success_url = '/account/'

    def get_context_data(self, **kwargs):

        context = super().get_context_data(**kwargs)

        context['submit_text'] = 'Confirm'
        context['title'] = 'Password'
        context['success_url'] = self.success_url
        context['message'] = 'Change your password'
        context['year'] = datetime.now().year

        return context

    def get_form_kwargs(self):

        """This allows for the user to be passed to the Form so clean validation
        can be done on it. """

        kwargs = super(AccountPasswordView, self).get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs

    ## POST level methods
    def form_valid(self, form):

        form.process_form(self.request)

        return super().form_valid(form)
