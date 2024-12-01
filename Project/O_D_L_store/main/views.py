from django.shortcuts import render


def index(request):
    return render(request, 'main/index.html')

def about(request):
    return render(request, 'main/about.html')

def contacts(request):
    return render(request, 'main/contacts.html')

def catalog(request):
    return render(request, 'main/catalog.html')

def profile(request):
    return render(request, 'main/profile.html')