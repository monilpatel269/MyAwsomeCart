from unicodedata import name
from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name="blogHome"),
    path("blogpost/<int:id>", views.blogpost, name="blogHome"),
    path('about/',views.about,name="AboutUs"),
    path('contact/',views.contact,name="ContactUs"),
    path('search/',views.search,name="Search"),
    path('signup/', views.handleSignUp, name="handleSignUp"),
    path('login/', views.handleLogIn, name="handleLogIn"),
    path('logout/', views.handleLogOut, name="handleLogOut"),
]