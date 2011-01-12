from django.conf.urls.defaults import *

from wiki.feeds import LatestArticlesFeed

urlpatterns = patterns('wiki.views',
    (r'^$', 'index'),
    (r'^feed/$', LatestArticlesFeed()),
    url(r'^search/$', 'search', name='search'),
    url(r'^(?P<slug>\w+)/pdf/$', 'create_pdf', name='create_pdf'),
    url(r'^wiki/(?P<slug>\w+)/$', 'view_article', name='view_article'),
    url(r'^edit/(?P<slug>\w+)/$', 'edit_article', name='edit_article'),
)
