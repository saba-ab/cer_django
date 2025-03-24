from django.conf import settings

from app.urls import path
from django.conf.urls.static import static
from . import views
urlpatterns = [
    path("", view=views.blog_index, name="blog"),
    path("<slug:slug>", view=views.blog_detail, name="detail"),
]
