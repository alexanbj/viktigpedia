# -*- coding: utf-8 -*-

from django.conf import settings
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.db import IntegrityError
from django.db.models import Q

from easymode.xslt.response import render_to_response
from easymode.tree import xml

from wiki.models import Article
from wiki.utils import xslt_param_builder
from wiki.utils import split_keywords

#try:
#    WIKI_LOCK_DURATION = settings.WIKI_LOCK_DURATION
#except AttributeError:
#    WIKI_LOCK_DURATION = 15
#
#class EditLock():

def index(request):
    articles = Article.objects.all()
    if request.method == 'POST':
        if request.POST['query']:
            articles =  search(request.POST['query'])
    print xml(articles)
    return render_to_response('base.xsl', articles)

def view_article(request, slug):
    edit_url = reverse('edit_article', args=[slug])
    try:
        # Enables case-insentivity
        article = Article.objects.get(slug=slug)
        if article.slug != slug:
            return HttpResponseRedirect(reverse('view_article', args=[article.slug]))

        params = {'editurl' : xslt_param_builder(edit_url)}
        return render_to_response('article.xsl', article, params)

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

    return render_to_response('edit_article.xsl', article, params)

def search(query):
    keywords = split_keywords(query)
    for keyword in keywords:
        title = Q(title__icontains=keyword)
        content = Q(content__icontains=keyword)
        articles = Article.objects.filter(title | content)

    return articles
