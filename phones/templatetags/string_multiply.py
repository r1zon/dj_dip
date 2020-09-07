from django.template import Library

register = Library()

@register.filter
def multiply(value, times):
    return value * times