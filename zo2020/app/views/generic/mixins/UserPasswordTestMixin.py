
from django.contrib.auth.mixins import UserPassesTestMixin

class UserPasswordTestMixin(UserPassesTestMixin):

    def test_func(self):
        
        user = self.request.user
        
        return not user.check_password(user.temporary_password)

    def handle_no_permission(self):

        return redirect('account-password')

