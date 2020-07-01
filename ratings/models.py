from django.db import models
from django.utils.safestring import mark_safe
from django.core.urlresolvers import reverse

from ratinguser.models import RatingUser

from decimal import Decimal

class Rating(models.Model):
    key = models.CharField(verbose_name='Rating Key', max_length=255, unique=True)
    total_rating = models.IntegerField(verbose_name='Total Rating Sum (computed)', default=0)
    total_votes = models.IntegerField(verbose_name='Total Votes (computed)', default=0)
    avg_rating = models.FloatField(verbose_name='Average Rating (computed)', default=0.0)
    percent = models.FloatField(verbose_name='Percent Fill (computed)', default=0.0)

    def __unicode__(self):
        """ Used to identify the object in admin forms. """
        return self.key

    def sanitize(self):
        if self.avg_rating < Decimal("0.0"):
            raise ValidationError("Average rating can not be negative")
        if self.percent < 0.0:
            raise ValidationError("Percent can not be negative")

    
    def save(self, *args, **kwargs):
        try:
            self.sanitize()
        except ValidationError, e:
            raise IntegrityError(e.messages)

        super(Rating, self).save(*args, **kwargs)


    def add_rating(self, event):
        self.total_rating = self.total_rating + event.value
        self.total_votes = self.total_votes + 1

        self.avg_rating = float(self.total_rating) / float(self.total_votes) / 20.0
        self.percent = float(self.avg_rating/5.0)


class RatingEvent(models.Model):
    """
    Each time someone votes, the vote will be recorded by ip address.
    Yes, this is not optimal for proxies, but good enough because if you
    are behind a proxy you should be working, and not rating stuff.
    """
    key = models.CharField(verbose_name='Rating Key', max_length=255)
    ip = models.IPAddressField()
    date = models.DateTimeField(auto_now_add=True)
    value = models.IntegerField(default=0)
    email = models.ForeignKey(RatingUser, null=True, blank=True)

    def __unicode__(self):
        """ Used to identify the object in admin forms. """
        return self.key + "_" + str(self.ip)

    def delete_vote(self):
        url = reverse('delete_vote', args=[self.id])
        return mark_safe(u'<a href="%s">%s</a>' % (url, 'Delete'))
    delete_vote.allow_tags = True

