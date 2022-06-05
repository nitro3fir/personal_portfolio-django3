from django.shortcuts import render
from .models import Project

def home(request):
    projects = Project.objects.all()
    return render(request, 'portfolio/home.html', {'projects': projects})

def detail(request, blog_id):
    return render(request, 'blog/detail.html', {'id': blog_id})
