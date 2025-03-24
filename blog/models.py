from django.db import models
from django.urls import reverse
from django.utils.text import slugify


class Blog(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True)
    content = models.TextField()
    source_url = models.URLField()
    youtube_url = models.URLField(blank=True, null=True)
    photo = models.ImageField(upload_to='blog_photos/', null=True, blank=True)
    published_at = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs) -> None:
        if not self.slug:
            base_slug = slugify(self.title)
            slug = base_slug
            count = 1
            while Blog.objects.filter(slug=slug).exists():
                slug = f"{base_slug}-{count}"
                count += 1
            self.slug = slug
        super().save(*args, **kwargs)

    def __str__(self) -> str:
        return self.title

    def get_absolute_url(self):
        return reverse("detail", kwargs={"slug": self.slug})