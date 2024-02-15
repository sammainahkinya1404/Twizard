from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.

# class PublishedManager(models.Manager):
#     def get_queryset(self):
#         return super().get_queryset()\
#         .filter(status=Post.Status.PUBLISHED)
    
# # Categories
   
# class Category (models.Model):
#     name=models.CharField(max_length=250)
# # Table Blog_posts
# class Post(models.Model):

#     # status of the blogpost
#     class Status(models.TextChoices):
#         DRAFT='DF','Draft'
#         PUBLISHED='PB','Published'



#     title=models.CharField(max_length=250)
#     categories=models.ManyToManyField(Category,on_delete=models.CASCADE)

#     slug=models.SlugField(max_length=250)
#     body=models.TextField()
#     author=models.ForeignKey(User,on_delete=models.CASCADE,related_name='blog_posts')
#     publish=models.DateTimeField(default=timezone.now())
#     created=models.DateTimeField(auto_now_add=True)
#     updated=models.DateTimeField(auto_now=True)
#     status=models.CharField(max_length=250,default=Status.DRAFT,choices=Status.choices)

#     objects = models.Manager() # The default manager.
#     published = PublishedManager() # Our custom manager.


#         # ordering blog posts from newest to oldest
#     class Meta:
#         ordering=['-publish']
#         indexes=[
#              models.Index(fields=['-publish'])
#              ]
        
#     def __str__(self):
#         return self.title
    
 
class Contacts(models.Model):
    name=models.CharField(max_length=250)
    email=models.CharField(max_length=250)
    msg=models.TextField(max_length=1000)
    date_sent=models.DateTimeField(auto_now_add=True)