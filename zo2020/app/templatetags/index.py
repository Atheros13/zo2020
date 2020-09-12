from django import template
from django.conf import settings

register = template.Library()

@register.filter(name='index')
def index(indexable, i):

    """Returns an item of index i from an iteratable object i.e. a list """

    return indexable[i]

