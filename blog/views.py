from django.shortcuts import render
from blog.models import *
from django.shortcuts import get_object_or_404

def blog_view(request):
    posts = Post.objects.filter(status=1)
    context = {'posts':posts}
    return render(request, 'blog/blog-home.html', context)

def blog_single(request,pid):
    post = get_object_or_404(Post, pk=pid, status=1)
    context = {'post':post}
    return render(request, 'blog/blog-single.html', context)

def blog_category(request,cat_name):
    posts = Post.objects.filter(status=1)
    posts = posts.filter(category__name=cat_name)
    context = {'posts':posts}
    return render(request, 'blog/blog-home.html', context)
