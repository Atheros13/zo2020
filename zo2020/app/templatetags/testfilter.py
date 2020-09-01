from django import template
from django.conf import settings

register = template.Library()

@register.filter(name='testfilter')
def testfilter(obj, value):
    
    '''Used for testing filters before writing them out properly '''

    return False