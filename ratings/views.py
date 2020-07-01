import sys, logging

from django.http import HttpResponse
from django.shortcuts import render_to_response, get_object_or_404, redirect
from django.db import transaction
from django.core import urlresolvers
from django.contrib import messages
from django.db.transaction import commit_manually
from django.views.decorators.csrf import csrf_exempt

from ratinguser.models import RatingUser

from .models import Rating, RatingEvent
from utils.decorators import key_required


@csrf_exempt
@commit_manually
@key_required
def record_vote(request):
    result = "success"
    try:
        rating, created = Rating.objects.get_or_create(key=request.POST['id'])
        key = request.POST['id']
        ip = request.META['REMOTE_ADDR']
        email = request.session['email']
        user = RatingUser.objects.filter(email=email)[0]
        event = RatingEvent.objects.create(key=key, ip=ip, email=user)
        event.value = int(request.POST['vote'])
        rating.add_rating(event)
        rating.save()
        event.save()
        result = "%.2f/5 rating" % (rating.avg_rating)
    except:
        transaction.rollback()
        result = 'error'
    else:
        transaction.commit()

    return HttpResponse(result)

def delete_vote(request, id):
    try:
        event = RatingEvent.objects.get(pk=id)
        rating = Rating.objects.get(key=event.key)
        rating.total_rating = rating.total_rating - event.value
        rating.total_votes = rating.total_votes - 1
        rating.avg_rating = float(rating.total_rating) / float(rating.total_votes) / 20.0
        rating.percent = float(rating.avg_rating/5.0)
        rating.save()
        event.delete()
    except ZeroDivisionError:
        messages.success(request, 'Sorry, You cannot delete the last vote.')
    else:
        messages.success(request, 'Vote has been deleted.')
    return redirect(urlresolvers.reverse('admin:index'))
