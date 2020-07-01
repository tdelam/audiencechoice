from django import forms
from django.conf import settings

from .models import RatingUser


class RatingUserForm(forms.ModelForm):
    class Meta:
        model = RatingUser
        exclude = ('activation_key', 'key_expires', 'is_confirmed', 'ip')