from django.conf.urls.defaults import *

urlpatterns = patterns('wiki.views',
    (r'^$', 'index'),
    url(r'^(?P<slug>\w+)/pdf/$', 'create_pdf', name='create_pdf'),
    url(r'^(?P<slug>\w+)/$', 'view_article', name='view_article'),
    url(r'^edit/(?P<slug>\w+)/$', 'edit_article', name='edit_article'),
)
