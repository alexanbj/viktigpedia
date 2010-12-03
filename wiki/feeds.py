from django.contrib.syndication.views import Feed

from wiki.models import Article

class LatestArticlesFeed(Feed):

    title = "Viktigpedia articles"
    link = "/feed/"
    description = "Updates on changes and additions to Viktigpedia"

    def items(self):
        return Article.objects.order_by('last_update')

    def item_title(self, item):
        return item.title

    def item_description(self, item):
        return item.rendered

    def item_pubdate(self, item):
        return item.created_at
