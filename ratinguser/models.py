import datetime

from django.db import models


class RatingUser(models.Model):
    email = models.EmailField(unique=False)
    activation_key = models.CharField(max_length=40, blank=True)
    key_expires = models.DateTimeField(default=datetime.datetime.now())
    ip = models.IPAddressField(blank=True, null=True)

    def __unicode__(self):
        return self.email