from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

posts = [
    {
        'author': 'JBrooksCS',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted': 'November 9th, 2020'
    },
    {
        'author': 'JBrooksCS',
        'title': 'Blog Post 2',
        'content': 'Second post content',
        'date_posted': 'November 10th, 2020'
    }

]

def home(request):
    context = {
        'posts': posts
    }
    return render(request, 'blog/home.html', context)

def about(request):
    return render(request, 'blog/about.html')
    
    