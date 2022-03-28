from django.contrib import admin
from blog.models import Blogcomment, Post
# Register your models here.
admin.site.register((Post,Blogcomment))