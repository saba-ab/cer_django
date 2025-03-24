from django.core.paginator import Paginator
from django.shortcuts import render
from .models import Blog
from .services import currency_service


def blog_index(request):
    blogs = Blog.objects.order_by('-published_at')

    paginator = Paginator(blogs, 6)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    currencies = currency_service.get_currencies()

    render_data = {
        'page_obj': page_obj,
        'currencies': currencies
    }
    return render(request, 'pages/index.html', render_data)

def blog_detail(request, slug):

    blog = Blog.objects.get(slug=slug)
    currencies = currency_service.get_currencies()

    render_data = {
        'blog': blog,
        'currencies': currencies
    }
    return render(request, 'pages/detail.html', render_data)
