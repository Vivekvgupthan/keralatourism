from django.shortcuts import render

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def activities(request):
    return render(request, 'activities.html')

def places(request):
    return render(request, 'places.html')

def contact(request):
    return render(request, 'contact.html')

def login(request):
    return render(request, 'login.html')
