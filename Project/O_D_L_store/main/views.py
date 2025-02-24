from django.shortcuts import render
from .models import Product


def index(request):
    products = Product.objects.all
    return render(request, 'main/index.html', {'products':products})

def about(request):
    return render(request, 'main/about.html')

def contacts(request):
    return render(request, 'main/contacts.html')

def catalog(request):
    return render(request, 'main/catalog.html')

def profile(request):
    return render(request, 'main/profile.html')

def camera(request):
    return render(request, 'main/camera.html')