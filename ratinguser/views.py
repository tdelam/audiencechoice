import datetime

from django.shortcuts import render, redirect, get_object_or_404
from django.core import urlresolvers
from django.contrib import messages
from django.http import HttpResponse
from django.template import loader, Context
from django.core.mail import EmailMultiAlternatives
from django.conf import settings

from .models import RatingUser
from .forms import RatingUserForm

from utils import utils
from utils.decorators import key_required

def index(request, template_name):
    if request.method == 'POST':
        postdata = request.POST.copy()
        form = RatingUserForm(postdata)
        if form.is_valid():
            key_expires = datetime.datetime.today() + datetime.timedelta(30)
            user = form.save(commit=False)
            if user.email == settings.KIOSK_EMAIL:
                user.activation_key = 'letmein'
            else:
                user.activation_key = utils.activation_key(user)
            user.ip = request.META['REMOTE_ADDR']
            user.key_expires = key_expires
            form.save()
            if user.email == settings.KIOSK_EMAIL:
                request.session['email'] = settings.KIOSK_EMAIL
                request.session['key'] = 'letmein'
                return redirect(urlresolvers.reverse('films'))
            else:
                html_template = loader.get_template('ratinguser/email_notification.html')
                plain_template = loader.get_template('ratinguser/email_notification.txt')
                context = Context({
                    'instance': user,
                    'url': utils.get_full_path(),
                })
                subject, from_email, to = "[Cinefest Audience Choice] Activation required", settings.FROM_EMAIL, user.email

                html_content = html_template.render(context)
                plain_content = plain_template.render(context)

                msg = EmailMultiAlternatives(subject, plain_content, from_email, [to])
                msg.attach_alternative(html_content, "text/html")
                msg.send()  
                messages.success(request, "Thank you. We've sent a verification link to your email address.")
                return redirect(urlresolvers.reverse('index'))
    else:
        form = RatingUserForm()
    return render(request, template_name, {
        'form': form
    })


def confirm(request, key):
    voter = get_object_or_404(RatingUser, activation_key=key)
    if voter.key_expires < datetime.datetime.today():
        messages.success(request, 'Sorry, your key has expired')
        return redirect(urlresolvers.reverse('index'))
    else:
        voter.save()
        request.session['email'] = voter.email
        request.session['key'] = key
        return redirect(urlresolvers.reverse('films'))


@key_required
def destroy_session(request):
    try:
        voter = RatingUser.objects.filter(activation_key__iexact=request.session.get('key', ''))[0]
        if voter.email != settings.KIOSK_EMAIL:
            voter.activation_key = '' # clear key so it's not longer valid
        voter.save()
        del request.session['email']
        del request.session['key']
    except KeyError:
        pass
    messages.success(request, 'Thank you. Your votes have been recorded.')
    return redirect(urlresolvers.reverse('index'))