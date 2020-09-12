from django.http import HttpRequest
from django.shortcuts import render, redirect
from django.views.generic.edit import FormView

from datetime import datetime
from django.contrib.auth.mixins import UserPassesTestMixin

from app.forms.account import AccountHubsOpenForm

class AccountHubsOpenView(UserPassesTestMixin, FormView):

    template_name = 'generic/basic-form.html'
    form_class = AccountHubsOpenForm
    success_url = '/hub'

    title = 'Open Hub'
    message = 'Choose from any Hubs that you have admin rights to.'

    ## CONTEXT
    def get_context_data(self, **kwargs):

        context = super().get_context_data(**kwargs)

        context["form"] = AccountHubsOpenForm(self.request.user)
        context['submit_text'] = 'Open Hub'
        context['title'] = self.title
        context['success_url'] = self.success_url
        context['message'] = self.message
        context['year'] = datetime.now().year

        return context

    def get_form_kwargs(self):

        """ """

        kwargs = super(AccountHubsOpenView, self).get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs

    ## POST
    def form_valid(self, form, *args, **kwargs):

        hub_id = form.process_form(self.request)
        self.request.session['hub'] = hub_id

        return super().form_valid(form)

    ## UserPassesTestMixin
    def test_func(self):
        
        user = self.request.user
        
        return not user.check_password(user.temporary_password)

    def handle_no_permission(self):

        return redirect('account-password')

