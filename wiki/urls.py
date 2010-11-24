from django.conf.urls.defaults import *

urlpatterns = patterns('wiki.views',
    (r'^$', 'index'),
    (r'^(?P<id>\d+)/$', 'view_article'),
    (r'^edit/(?P<id>\d+)/$', 'edit_article'),
)
