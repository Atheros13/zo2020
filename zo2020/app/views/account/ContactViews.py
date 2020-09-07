from django.views.generic.edit import FormView
from django.shortcuts import render, redirect

from datetime import datetime

from app.forms.account import AccountContactForm
from app.views.generic import GenericContactSentView

from django.contrib.auth.mixins import UserPassesTestMixin

class AccountContactView(UserPassesTestMixin, FormView):

    template_name = 'generic/basic-form.html'
    form_class = AccountContactForm
    success_url = '/account/contact/sent'

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

    def test_func(self):
        
        user = self.request.user
        
        return not user.check_password(user.temporary_password)

    def handle_no_permission(self):

        return redirect('account-password')

class AccountContactSentView(GenericContactSentView):

    next_url_name = 'account-home'    