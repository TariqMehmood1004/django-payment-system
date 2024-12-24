from django import template

register = template.Library()

@register.filter(name='strip_quotes')
def strip_quotes(value):
    """Strips unwanted characters like [" and \ from the string."""
    if isinstance(value, str):
        return value.strip('["\\"')
    return value
