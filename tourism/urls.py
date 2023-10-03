from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('activities/', views.activities, name='activities'),
    path('places/', views.places, name='places'),
    path('contact/', views.contact, name='contact'),
    path('login/', views.login, name='login'),
]
