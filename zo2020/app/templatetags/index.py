from django import template
from django.conf import settings

register = template.Library()

@register.filter(name='index')
def index(indexable, i):

    print(indexable, i)

    return indexable[i]

