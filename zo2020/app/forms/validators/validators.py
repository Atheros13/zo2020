from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

from app.models import User, Hub

def is_user(value):

    if not User.objects.filter(email=value):
        raise ValidationError(
                    _('There is no account found for %(value)s'),
                    params={'value': value},
                )

def unique_user(value):

    if User.objects.filter(email=value).first() != None:
        raise ValidationError(
                    _('%(value)s already has an account'),
                    params={'value': value},
                )

def unique_hub_email(value):

    """Checks that each Hub has a unique email address """
    if Hub.objects.filter(email=value).first() != None:

        error_message = 'A Hub with %(value)s as the contact email already exists, or has been requested.'

        raise ValidationError(
                    _(error_message),
                    params={'value': value},
                )

