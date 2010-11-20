from easymode.xslt.response import render_to_response
from easymode.tree import xml

from wiki.models import Article

def index(request):
    articles = Article.objects.all()
    return render_to_response('model-to-xml.xsl', articles)
