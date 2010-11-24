from django.db import models
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify

from easymode.tree.decorators import toxml

@toxml
class Article(models.Model):
    title = models.CharField(max_length=200)

    summary = models.TextField()
    content = models.TextField()
    creator = models.ForeignKey(User, verbose_name='Article Creator')
    created_at = models.DateTimeField(auto_now_add=True)
    last_update = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return self.title
