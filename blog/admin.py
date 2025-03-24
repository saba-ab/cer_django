from django.contrib import admin
from .models import Blog
from unfold.admin import ModelAdmin


@admin.register(Blog)
class BlogAdmin(ModelAdmin):
    list_display = ('title', 'slug', 'published_at')
    prepopulated_fields = {'slug': ('title',)}