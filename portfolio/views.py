from django.shortcuts import render
from .models import Project, Script

def home(request):
    projects = Project.objects.all()
    scripts = Script.objects.all()
    return render(request, 'portfolio/home.html', {'projects': projects, 'scripts': scripts})

def detail(request, blog_id):
    return render(request, 'blog/detail.html', {'id': blog_id})
