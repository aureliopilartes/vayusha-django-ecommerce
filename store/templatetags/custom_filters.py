from django import template
from django.utils import numberformat

register = template.Library()

@register.filter
def format_price(value):
    return numberformat.format(value, ",", grouping=3, force_grouping=True, decimal_pos=2)
