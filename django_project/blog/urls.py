from django.urls import path
from . import views

urlpatterns = [
    #After leaving django_project/urls.py, remainder of string 
    #is passed here to find attempted match
    path('', views.home, name='blog-home'),
    path('about', views.about, name='blog-about'),
]