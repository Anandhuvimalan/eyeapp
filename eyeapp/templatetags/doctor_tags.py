import re

from django import template

register = template.Library()

IMG_TAG = re.compile(r'<img\b[^>]*>', re.IGNORECASE)


@register.filter
def strip_images(html):
    """Remove <img> tags from rich text."""
    return IMG_TAG.sub('', html or '')
