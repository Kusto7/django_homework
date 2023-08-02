from django import template
from django.conf import settings

register = template.Library()


@register.filter
def mediapath(value):
    media_url = settings.MEDIA_URL
    media_path = f"{media_url}{value}"

    return media_path
