from django.conf.urls.defaults import *

urlpatterns = patterns('films.views',
    url(r'^$', 'index', { 'template_name': 'films/index.html' }, 'films'),
    url(r'^category/(?P<category_slug>[-\w]+)/$', 'show_category', { 'template_name':'films/category.html' }, 'film_category'),
)
