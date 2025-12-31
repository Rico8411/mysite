from django.shortcuts import render
from blog.models import (Post, category)
from django.shortcuts import get_object_or_404
from django.core.paginator import( Paginator, EmptyPage, PageNotAnInteger)


def blog_view(request, cat_name=None, author_name=None):
    posts = Post.objects.filter(status=1)
    categories = category.objects.all()
    if cat_name:
        posts = posts.filter(category__name=cat_name)
    if author_name:
        posts = posts.filter(author__username=author_name)

    posts = Paginator(posts, 3)
    page_number = request.GET.get('page')

    try:
        posts = posts.get_page(page_number)
    except PageNotAnInteger:
        posts = posts.get_page(1)
    except EmptyPage:
        posts = posts.get_page(1)
    context = {'posts':posts, 'categories':categories}
    return render(request, 'blog/blog-home.html', context)

def blog_single(request, pid):
    post = get_object_or_404(Post, pk=pid, status=1)
    categories = category.objects.all()
    context = {'post':post, 'categories':categories}
    return render(request, 'blog/blog-single.html', context)

def blog_search(request):
    posts = Post.objects.filter(status=1)
    if request.method == 'GET':
        posts = posts.filter(content__contains=request.GET.get('s'))
    context = {'posts':posts}
    return render(request, 'blog/blog-home.html', context)
