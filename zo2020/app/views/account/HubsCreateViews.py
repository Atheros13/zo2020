from django.http import HttpRequest
from django.shortcuts import render, redirect
from django.views.generic.edit import FormView

from datetime import datetime
from django.contrib.auth.mixins import UserPassesTestMixin

from app.forms.account import AccountHubsCreateForm
from app.views.generic import GenericContactSentView

class AccountHubsCreateView(UserPassesTestMixin, FormView):

    template_name = 'generic/basic-form.html'
    form_class = AccountHubsCreateForm
    success_url = '/account/hubs/create/request-sent'

    title = 'Create Hub'
    message = 'Create Hub Message'

    def get_context_data(self, **kwargs):

        context = super().get_context_data(**kwargs)

        context['submit_text'] = 'Send Request'
        context['title'] = self.title
        context['success_url'] = self.success_url
        context['message'] = self.message
        context['year'] = datetime.now().year

        return context

    def get_form_kwargs(self):

        """This allows for the user to be passed to the Form so clean validation
        can be done on it. """

        kwargs = super(AccountHubsCreateView, self).get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs

    ## POST level methods
    def form_valid(self, form):

        form.process_form(self.request)

        return super().form_valid(form)

    def test_func(self):
        
        user = self.request.user
        
        return not user.check_password(user.temporary_password)

    def handle_no_permission(self):

        return redirect('account-password')

class AccountHubsCreateSentView(UserPassesTestMixin, GenericContactSentView):

    title = 'Hub Request Sent'
    message = 'You will only receive a confirmation email if this request is accepted. It may take up to 72 hours to hear back.'
    next_url_name = 'account-home' 