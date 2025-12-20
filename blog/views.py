from django.shortcuts import render
from blog.models import *
from django.shortcuts import get_object_or_404

def blog_view(request, cat_name=None, author_name=None):
    posts = Post.objects.filter(status=1)
    if cat_name:
        posts = posts.filter(category__name=cat_name)
    if author_name:
        posts = posts.filter(author__username=author_name)
    context = {'posts':posts}
    return render(request, 'blog/blog-home.html', context)

def blog_single(request, pid):
    post = get_object_or_404(Post, pk=pid, status=1)
    context = {'post':post}
    return render(request, 'blog/blog-single.html', context)

# def blog_category(request,cat_name):
    posts = Post.objects.filter(status=1)
    posts = posts.filter(category__name=cat_name)
    context = {'posts':posts}
    return render(request, 'blog/blog-home.html', context)
