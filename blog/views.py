from django.shortcuts import render
from blog.models import (Post, category, Comment)
from django.shortcuts import get_object_or_404
from django.core.paginator import( Paginator, EmptyPage, PageNotAnInteger)
from django.contrib import messages
from blog.forms import CommentForm


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
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your comment has been submitted successfully')
        else:
            messages.error(request, 'There was an error submitting your comment')
    
    post = get_object_or_404(Post, pk=pid, status=1)
    categories = category.objects.all()
    comments = Comment.objects.filter(post=post, approved=True)
    form = CommentForm()
    context = {'post':post, 'categories':categories, 'comments':comments, 'form':form}
    return render(request, 'blog/blog-single.html', context)

def blog_search(request):
    posts = Post.objects.filter(status=1)
    if request.method == 'GET':
        posts = posts.filter(content__contains=request.GET.get('s'))
    context = {'posts':posts}
    return render(request, 'blog/blog-home.html', context)
