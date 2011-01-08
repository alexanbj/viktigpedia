# -*- coding: utf-8 -*-

from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.conf import settings

from easymode.tree.decorators import toxml
import tweepy

from wiki.utils import slugify

@toxml
class Article(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(editable=False, max_length=200)

    content = models.TextField()
    rendered = models.TextField(editable=False, blank=True)
    creator = models.ForeignKey(User, verbose_name='Article Creator')
    created_at = models.DateTimeField(auto_now_add=True)
    last_update = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return self.title

    def save(self, *args, **kwargs):
        from markdown import markdown
        self.rendered = markdown(self.content, ['footnotes', 'toc', 'wikilinks',])
        self.slug = slugify(self.title)
        super(Article, self).save(*args, **kwargs)

    @models.permalink
    def get_absolute_url(self):
        return ('view_article', [self.slug])


def tweet(sender, **kwargs):
    """Issue a tweet when a new article is saved."""
    print kwargs

    if kwargs['created']:
        auth = tweepy.OAuthHandler(settings.TWITTER_CONSUMER_KEY, settings.TWITTER_CONSUMER_SECRET)

        auth.set_access_token(settings.TWITTER_ACCESS_KEY, settings.TWITTER_ACCESS_SECRET)

        api = tweepy.API(auth)
        obj = kwargs['instance']
        lol = api.update_status(obj.title)
        print lol

post_save.connect(tweet, sender=Article)
