from django.conf import settings
from django.shortcuts import render
from django.http import HttpResponse




def home(request):
    print("Home View | Started :)")
    return render(request, "home.html", {'title': 'Home'})


