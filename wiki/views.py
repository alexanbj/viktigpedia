# -*- coding: utf-8 -*-

import cStringIO
import StringIO

from django.conf import settings
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from django.core.urlresolvers import reverse
from django.db import IntegrityError
from django.db.models import Q
from django.shortcuts import get_object_or_404

from easymode.xslt.response import render_to_string
from easymode.tree import xml

from rml import rml2pdf

from wiki.models import Article
from wiki.utils import xslt_param_builder
from wiki.utils import split_keywords
from wiki.utils import render_to_response

#try:
#    WIKI_LOCK_DURATION = settings.WIKI_LOCK_DURATION
#except AttributeError:
#    WIKI_LOCK_DURATION = 15
#
#class EditLock():

def index(request):
    articles = Article.objects.all()
    if request.method == 'POST':
        if getattr(request.POST, 'query', None):
            articles =  search(request.POST['query'])
    print xml(articles)
    return render_to_response(request, 'base.xsl', articles)

def view_article(request, slug):
    if 'pdf' in request.GET:
        return pdf(request)
    edit_url = reverse('edit_article', args=[slug])
    try:
        # Enables case-insentivity
        article = Article.objects.get(slug=slug)
        if article.slug != slug:
            return HttpResponseRedirect(reverse('view_article', args=[article.slug]))

        params = {'editurl' : xslt_param_builder(edit_url)}
        print xml(article)
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


    if request.method == 'POST':
        article.title = request.POST['title']
        article.content = request.POST['content']
        article.save()
        view_url = reverse('view_article', args=[article.slug])
        return HttpResponseRedirect(view_url)

    view_url = reverse('view_article', args=[slug])
    params = {'viewurl' : xslt_param_builder(view_url)}

    return render_to_response(request, 'edit_article.xsl', article, params)

def create_pdf(request, slug):
    """Returns article as PDF, with the help of RML markup."""

    # We only allow PDF creation of existing articles
    article = get_object_or_404(Article, slug__iexact=slug)

    # Generate RML of article
    rml = StringIO.StringIO(render_to_string('rml.xsl', article))

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

def search(query):
    """Returns articles matching query."""
    keywords = split_keywords(query)
    for keyword in keywords:
        title = Q(title__icontains=keyword)
        content = Q(content__icontains=keyword)
        articles = Article.objects.filter(title | content)

    return articles
