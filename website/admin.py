from django.contrib import admin
from .models import *


class ContactAdmin(admin.ModelAdmin):
    date_hierarchy = 'created_date'
    list_display = ('id','name', 'email','created_date')
    list_filter =('email',)
    search_fields = ('name','message')
    

admin.site.register(Contact, ContactAdmin)

# Register your models here.
