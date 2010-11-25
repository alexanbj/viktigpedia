# -*- coding: utf-8 -*-

import StringIO

from django.conf import settings
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.db import IntegrityError

from easymode.xslt.response import render_to_response
from easymode.xslt.response import render_xml_to_string
from easymode.xslt import prepare_string_param as q
from easymode.utils.xmlutils import XmlPrinter
#from easymode.tree import xml

from wiki.models import Article

#try:
#    WIKI_LOCK_DURATION = settings.WIKI_LOCK_DURATION
#except AttributeError:
#    WIKI_LOCK_DURATION = 15
#
#class EditLock():

def index(request):
    articles = Article.objects.all()
    return render_to_response('base.xsl', articles)

def view_article(request, title):
    edit_url = reverse('edit_article', args=[title])
    try:
        article = Article.objects.get(title=title)
        stream = StringIO.StringIO()
        xml = XmlPrinter(stream, settings.DEFAULT_CHARSET)
        xml.characters(edit_url)

        params = {'editurl' : q(stream.getvalue().decode('utf-8'))}
        return render_to_response('article.xsl', article, params)

    # If the article does not exist, we go to edit mode
    except Article.DoesNotExist:
        return HttpResponseRedirect(edit_url)

def edit_article(request, title):
    article = None
    try:
        article = Article.objects.get(title=title)
    except Article.DoesNotExist:
        article = Article(title=title, creator=request.user)
    if request.method == 'POST':
        article.title = request.POST['title']
        article.content = request.POST['content']
        article.save()
        return HttpResponseRedirect(reverse('view_article', args=(article.title,)))
    return render_to_response('edit_article.xsl', article)
