from django import template
from django.conf import settings

from ratings.models import Rating, RatingEvent

register = template.Library()

def show_rating(context, rating_key):
    """
    displays necessary html for the rating
    """
    rating, created = Rating.objects.get_or_create(key=rating_key)
    return {
        'rating_key': rating_key,
        'total_votes': rating.total_votes,
        'total_ratings': rating.total_rating,
        'rating': rating.avg_rating,
        'percent': rating.percent,
        'max_stars': 5
        }
register.inclusion_tag("ratings/rating.html", takes_context=True)(show_rating)

def rating_header(context):
    """
    Inserts the includes needed into the html
    """
    return { 'ratings_media_url': settings.MEDIA_URL }

register.inclusion_tag("ratings/rating_header.html", takes_context=True)(rating_header)

