from django import template
from blog.models import Post, category
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


@register.inclusion_tag("blog/blog-post-categories.html")
def post_categories():
    posts = Post.objects.filter(status=1)
    categories = category.objects.all()
    cat_dict = {}
    for name in categories:
        cat_dict[name] = posts.filter(category=name).count()
    return {'categories':cat_dict}
        