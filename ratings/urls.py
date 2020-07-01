from django.conf.urls.defaults import *

urlpatterns = patterns('',
    url(r'^submit', 'ratings.views.record_vote'),
    url(r'^delete/(?P<id>\d+)/$', 'ratings.views.delete_vote', {}, name='delete_vote'),
)
