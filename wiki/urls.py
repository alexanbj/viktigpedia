from django.conf.urls.defaults import *

urlpatterns = patterns('wiki.views',
    (r'^$', 'index'),
    (r'^(?P<id>\d+)/$', 'view_article'),
    url(r'^(?P<title>\w+)/$', 'view_article', name='view_article'),
    url(r'^edit/(?P<title>\w+)/$', 'edit_article', name='edit_article'),
)
