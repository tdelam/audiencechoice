from django import template

from films.models import Category

register = template.Library()

@register.inclusion_tag("tags/nav.html")
def categories(request_path):
    active_categories = Category.objects.all()
    return {
        'active_categories': active_categories,
        'request_path': request_path
        }
