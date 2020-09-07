from django import template

register = template.Library()

@register.filter(name='nav_menu_url')
def nav_menu_url(menu, heading):

    print(menu)
    print(heading)
    return menu[heading][0]

