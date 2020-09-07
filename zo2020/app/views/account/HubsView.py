from django.http import HttpRequest
from django.shortcuts import render, redirect
from django.views import View

from datetime import datetime
from django.contrib.auth.mixins import UserPassesTestMixin

class AccountHubsView(UserPassesTestMixin, View):

    template_name = 'generic/basic-page.html'
    title = 'Hubs'

    def get(self, request, *args, **kwargs):

        return render(
            request,
            self.template_name,
            {
                'title':self.title,
                'year':datetime.now().year,
            }
        )

    def test_func(self):
        
        user = self.request.user
        
        return not user.check_password(user.temporary_password)

    def handle_no_permission(self):

        return redirect('account-password')

