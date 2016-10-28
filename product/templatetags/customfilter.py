from django import template
from django.template.defaultfilters import stringfilter

register = template.Library()


@register.filter(name='cut')
def cut(value, arg):
    return value.replace(arg, '')
