from django.contrib import admin
from django.urls import path, include
from . import views
urlpatterns = [

    path('', views.new_blog, name= 'blog'),
    path('create/', views.create_blog, name= 'blog'),
    path('list/', views.list_blog_doc, name= 'blog'),
    path('alllist/',views.list_blog_pat, name= 'blog')


]