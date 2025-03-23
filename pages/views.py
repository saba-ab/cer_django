from django.shortcuts import render


def home(request):
    return render(request, 'pages/home.html')

def about(request):
    return render(request, 'pages/about.html')

def blog(request):
    return render(request, 'pages/blog.html')

def services(request):
    return render(request, 'pages/services.html')

def products(request):
    return render(request, 'pages/products.html')