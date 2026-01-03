from django.contrib import admin
from blog.models import *
# Register your models here.


class PostAdmin(admin.ModelAdmin):
    
    date_hierarchy = 'created_date'
    empty_value_display = '-empty-'
    list_display = ('title','author','counted_views','status','published_date','created_date')
    list_filter = ('status','published_date')
    ordering = ('-created_date',)
    search_fields = ('title','content')


class CommentAdmin(admin.ModelAdmin):
    
    date_hierarchy = 'created_date'
    empty_value_display = '-empty-'
    list_display = ('name','email','subject','approved','created_date')
    list_filter = ('approved','created_date','post')
    ordering = ('-created_date',)
    search_fields = ('name','email','subject','message','post')

admin.site.register(category)
admin.site.register(Post,PostAdmin)
admin.site.register(Comment,CommentAdmin)
