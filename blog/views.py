from django.conf import settings
from django.shortcuts import render
from django.http import HttpResponse

from blog.models import Post


def home(request):
    print("Home View | Started :)")
    return render(request, "home.html", {'title': 'Home'})


def posts(request):
    return render(request, "posts.html", {'posts': Post.objects.all(), 'title': 'Posts'})
