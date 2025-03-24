import requests
from django.core.files.base import ContentFile
from django.core.management.base import BaseCommand
from blog.services.bmg_parser import fetch_blogs_from_bmg
from blog.models import Blog

class Command(BaseCommand):
    help = "Parse blogs from external sources."

    def handle(self, *args, **kwargs):
        blogs = fetch_blogs_from_bmg()
        for data in blogs:
            blog, created = Blog.objects.get_or_create(
                source_url=data.source_url,
                defaults={
                    "title": data.title,
                    "slug": data.slug,
                    "content": data.content,
                    "youtube_url": data.youtube_url,
                    "published_at": data.published_at,
                    "created_at": data.created_at,
                }
            )
            if created:
                try:
                    image_response = requests.get(data.photo_url)
                    if image_response.status_code == 200:
                        file_name = data.photo_url.split("/")[-1]
                        blog.photo.save(file_name, ContentFile(image_response.content), save=True)
                        self.stdout.write(f"✅ Saved image for: {data.title}")
                except Exception as e:
                    self.stdout.write(f"❌ Failed to download image for {data.title}: {e}")
