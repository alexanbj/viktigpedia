from django.db import models
from easymode.tree.decorators import toxml

@toxml
class Article(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()

    def __unicode__(self):
        return self.title
