from django.contrib.sitemaps import Sitemap

from blog.models import Blog


class BlogSitemap(Sitemap):
    def items(self):
        return Blog.objects.all()

    def lastmod(self, obj):
        return obj.published_at
