from django.contrib import admin
from django.urls import path
from notebook import views
urlpatterns = [
    path('', views.signup),
    path('signin', views.signin),
    path('home', views.home),
    path('logout', views.signout),
]