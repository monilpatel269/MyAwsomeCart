from unicodedata import name
from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name="blogHome"),
    path('blogpost/', views.blogpost,name="blogPost"),
]