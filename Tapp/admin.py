from django.contrib import admin
from .models import Contacts

# # Register your models here.

# class PostAdmin(admin.ModelAdmin):
#     list_display=['title','slug','author','status','publish','created','updated','categories']
#     prepopulated_fields={'slug':('title',)}
#     ordering=['status','publish']

# admin.site.register(Post, PostAdmin)
class ContsAdmin(admin.ModelAdmin):
    list_display=['name','email','msg','date_sent']
    
admin.site.register(Contacts,ContsAdmin)