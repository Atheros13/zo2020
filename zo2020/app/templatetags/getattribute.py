from django import template
from django.conf import settings

register = template.Library()

@register.filter(name='getattribute')
def getattribute(obj, attr_name):
    
    '''Template Tag: Returns the attribute of an object 
    based on the string of it's name. Returns
      
    stackoverflow.com/questions/844746 fotinakis'''

    print(attr_name)

    if hasattr(obj, str(attr_name)):
        return getattr(obj, attr_name)

    return False