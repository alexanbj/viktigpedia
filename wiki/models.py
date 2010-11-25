# -*- coding: utf-8 -*-

from django.db import models
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify

from easymode.tree.decorators import toxml

@toxml
class Article(models.Model):
    title = models.CharField(max_length=200)

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
        super(Article, self).save(*args, **kwargs)
