from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

from app.models import User

def unique_user(value):

    if User.objects.filter(email=value).first() != None:
        raise ValidationError(
                    _('%(value)s already has an account'),
                    params={'value': value},
                )
