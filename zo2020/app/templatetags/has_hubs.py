from django import template
from django.conf import settings

from app.models import Hub

register = template.Library()

@register.filter(name='has_hubs')
def has_hubs(user):

    """Returns True if the user.account is found in any admins field 
    in any Hub AND if that Hub is active i.e. not still in the request stage. 
    Returns False otherwise. """

    if Hub.objects.filter(admins=user.account).filter(is_active=True):
        return True
    return False

