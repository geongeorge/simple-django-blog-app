from django.http import HttpResponse
from django.shortcuts import render
from .models import Posts

def index(request):
    posts = Posts.objects.all()[:10]

    context = {
        'title' : 'Latest Posts',
        'posts': posts
    }
    return  render(request, 'posts/index.html', context)
    
def show(request,id):
    post = Posts.objects.get(id=id)

    context = {
        'title' : post.title,
        'body': post.body,
        'date' : post.created_at
    }
    return  render(request, 'posts/post.html', context)