from django import template
from blog.models import Post
register = template.Library()

# @register.simple_tag(name='posts')
# def func():
#     post = Post.objects.filter(status=1).count()


# @register.filter
# def value(value,args=100):
#     return value[args]



@register.inclusion_tag("blog/blog-popular-posts.html")
def latestposts(args=3):
    posts = Post.objects.filter(status=1).order_by('published_date')[:args]
    return{'posts':posts}
