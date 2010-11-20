from django.conf.urls.defaults import *

urlpatterns = patterns('wiki.views',
    (r'^$', 'index'),
)
