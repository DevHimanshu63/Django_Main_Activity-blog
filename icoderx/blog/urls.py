from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [

     path('', views.blogHome, name='blogHome'),
     path('<str:slug>', views.blogpost, name='blogpost'),
     path('postcomment',views.postcomment,name="postcomment"),
]

