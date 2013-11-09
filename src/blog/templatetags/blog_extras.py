import bleach
import markdown2
from django import template
from django.template.defaultfilters import stringfilter
from django.utils.safestring import mark_safe

register = template.Library()


@register.filter(is_safe=True)
@stringfilter
def markdown(input):
    sanitized_input = bleach.clean(input)
    return mark_safe(markdown2.markdown(sanitized_input))
