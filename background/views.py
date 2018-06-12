from django.shortcuts import render
from django.views.generic import TemplateView

def postList(request):
    return render(request, 'background/postList.html', {})

def about(request):
    return render(request, 'background/about.html', {})

def index(request):
    return render(request, 'background/index.html', {})



