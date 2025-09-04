from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from blog.views import *


app_name = 'blog'

urlpatterns = [
    path('', blog_view, name='index'),
    path('blog/single', blog_single, name='single'),
]