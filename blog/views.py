from django.shortcuts import render, get_object_or_404
from .models import Post

def all_blogs(request):
    posts_count = Post.objects.count
    posts = Post.objects.order_by('-date')[:5]
    return render(request, 'blog/all_blogs.html', {'posts': posts, 'posts_count':posts_count})

def detail(request, blog_id):
    post = get_object_or_404(Post, pk=blog_id)
    return render(request, 'blog/detail.html', {'post': post})