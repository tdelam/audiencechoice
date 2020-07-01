from django.conf.urls.defaults import *

urlpatterns = patterns('ratinguser.views',
    url(r'^$', 'index', { 'template_name': 'ratinguser/index.html' }, 'index'),
    url(r'^confirm/(?P<key>[-\w]+)/$', 'confirm', {}, 'confirm'), 
    url(r'^destroy-session', 'destroy_session', {}, 'destroy_session'),
)
