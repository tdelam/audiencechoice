from django.contrib.auth.decorators import login_required
from django.core import urlresolvers
from django.contrib import messages
from django.shortcuts import redirect, get_object_or_404
from django.utils.functional import wraps
from django.core.exceptions import MultipleObjectsReturned
from django.conf import settings

from ratinguser.models import RatingUser


def key_required(function):
    def wrap(request, *args, **kwargs):
        voter = ''
        try:
            voter = RatingUser.objects.filter(activation_key__iexact=request.session.get('key', ''))[0]
        except (RatingUser.DoesNotExist, IndexError):
             messages.success(request, 'Sorry, You do not have permission to do that.')
             return redirect(urlresolvers.reverse('index'))
        else:
            if request.session.get('email', '') == settings.KIOSK_EMAIL and request.session.get('key', '') == settings.KIOSK_KEY:
                return function(request, *args, **kwargs)
            elif voter.email == request.session.get('email', '') and voter.activation_key == request.session.get('key', ''):
                return function(request, *args, **kwargs)
            else:
                messages.success(request, 'Sorry, You do not have permission to do that.')
                return redirect(urlresolvers.reverse('index'))    
    wrap.__doc__=function.__doc__
    wrap.__name__=function.__name__
    return wrap