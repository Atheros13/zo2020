from django import template
from django.conf import settings

register = template.Library()

@register.filter(name='url_level')
def url_level(obj):

    """Returns a string value indicating which level of the website the page 
    is on i.e. account or hub etc.  """

    url_parts = obj.split('/')
    if len(url_parts) > 1:
        return obj.split('/')[1]
    else:
        return None