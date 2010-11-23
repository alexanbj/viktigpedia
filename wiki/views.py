from django.conf import settings

from easymode.xslt.response import render_to_response
from easymode.tree import xml

from wiki.models import Article

#try:
#    WIKI_LOCK_DURATION = settings.WIKI_LOCK_DURATION
#except AttributeError:
#    WIKI_LOCK_DURATION = 15
#
#class EditLock():


def index(request):
    articles = Article.objects.all()
    print xml(articles)
    return render_to_response('base.xsl', articles)
