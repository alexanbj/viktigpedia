# -*- coding: utf-8 -*-

import cStringIO
import StringIO
import datetime

from django.conf import settings
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from django.core.urlresolvers import reverse
from django.core.cache import cache
from django.db import IntegrityError
from django.db.models import Q
from django.shortcuts import get_object_or_404

from easymode.xslt.response import render_to_string
from easymode.xslt.response import render_xml_to_string
from easymode.tree import xml


from wiki.models import Article
from wiki.utils import xslt_param_builder
from wiki.utils import split_keywords
from wiki.utils import render_to_response

try:
    WIKI_LOCK_DURATION = settings.WIKI_LOCK_DURATION
except AttributeError:
    WIKI_LOCK_DURATION = 15

class EditLock():
    def __init__(self, title, request):
        self.title = title
        self.created_at = datetime.datetime.now()
        self.ip = request.META['REMOTE_ADDR']

        cache.set(title, self, WIKI_LOCK_DURATION*60)

    def is_mine(self, request):
        return self.ip == request.META['REMOTE_ADDR']

def index(request):
    articles = Article.objects.all()
    if request.method == 'POST':
        if getattr(request.POST, 'query', None):
            articles =  search(request.POST['query'])
    #print xml(articles)
    return render_to_response(request, 'base.xsl', articles)

def view_article(request, slug):
    edit_url = reverse('edit_article', args=[slug])
    try:
        # Enables case-insentivity
        article = Article.objects.get(slug__iexact=slug)
        if article.slug != slug:
            return HttpResponseRedirect(reverse('view_article', args=[article.slug]))

        params = {'editurl' : xslt_param_builder(edit_url)}
        #print xml(article)
        return render_to_response(request, 'article.xsl', article, params)

    # If the article does not exist, we go to edit mode
    except Article.DoesNotExist:
        return HttpResponseRedirect(edit_url)

def edit_article(request, slug):
    article = None

    try:
        # Enables case-insentivity
        article = Article.objects.get(slug__iexact=slug)
        if article.slug != slug:
            return HttpResponseRedirect(reverse('edit_article', args=[article.slug]))
    except Article.DoesNotExist:
        title = slug.replace('_', ' ')
        article = Article(title=title, creator=request.user)

    if request.method == 'GET':

        # Check mutual exclusion
        lock = cache.get(article.title, None)
        if lock is None:
            lock = EditLock(article.title, request)
        elif not lock.is_mine(request):
            print "Possible editing conflict. Another user started editing", lock.created_at

    elif request.method == 'POST':
        article.title = request.POST['title']
        article.content = request.POST['content']
        article.save()

        cache.delete(article.title)

        view_url = reverse('view_article', args=[article.slug])
        return HttpResponseRedirect(view_url)

    view_url = reverse('view_article', args=[slug])
    params = {'viewurl' : xslt_param_builder(view_url)}

    return render_to_response(request, 'edit_article.xsl', article, params)

def search(request):

    if request.method == 'POST':
        result = query(request.POST['query'])

        # Redirect straight to single result
        if len(result) == 1:
            view_url = reverse('view_article', args=[result[0].slug])
            return HttpResponseRedirect(view_url)


        params = {'query' : xslt_param_builder(request.POST['query'])}
        #print result
        #print xml(result)

        return render_to_response(request, 'search.xsl', result, params)

def create_pdf(request, slug):
    """Returns article as PDF, with the help of RML markup."""

    from rml import rml2pdf

    # We only allow PDF creation of existing articles
    article = get_object_or_404(Article, slug__iexact=slug)

    # Create XML of article, with content unescaped
    unescaped_article = render_to_string('article-to-xml.xsl', article)

    # Generate RML of article
    format = "%a, %d %b %Y %H:%M:%S"
    timestamp = datetime.datetime.today().strftime(format)
    params = {'timestamp' : xslt_param_builder(timestamp)}
    rml = StringIO.StringIO(render_xml_to_string('rml.xsl', unescaped_article, params))

    # Create the PDF
    buf = cStringIO.StringIO()
    rml2pdf.go(rml, outputFileName=buf)
    buf.seek(0)
    pdf = buf.read()
    buf.close()

    # Set up response object
    response = HttpResponse(mimetype='application/pdf')
    response.write(pdf)
    response['Content-Disposition'] = ('attachment; filename=%s.pdf' % article.title)
    return response

def query(query):
    """Returns articles matching query."""
    keywords = split_keywords(query)
    for keyword in keywords:
        title = Q(title__icontains=keyword)
        content = Q(content__icontains=keyword)
        articles = Article.objects.filter(title | content)

    return articles
