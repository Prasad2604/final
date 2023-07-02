from django.contrib import admin
from django.urls import path
from shops import views

urlpatterns = [
    path("", views.index, name="home"),
    path("cafe", views.cafe, name="cafe"),
    path("restaurant", views.restaurant, name="restaurant"),
    path("login", views.login, name="login"),
    path("ourteam", views.OurTeam, name="ourteam"),
    path("shakes", views.shakes, name="shakes"),
    path("cart", views.cart, name="cart"),
   
]
