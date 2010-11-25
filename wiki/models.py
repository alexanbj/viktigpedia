# -*- coding: utf-8 -*-

from django.db import models
from django.contrib.auth.models import User

from easymode.tree.decorators import toxml

from wiki.utils import slugify

@toxml
class Article(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(editable=False, serialize=False, max_length=200)

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
