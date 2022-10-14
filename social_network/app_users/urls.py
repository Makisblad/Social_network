from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('', test, name='test'),
    #path("/<str:slug>", user, name='test'),
    path("register/", register, name='register'),
    path("login/", login, name='login'),
    #path("register/", UserRegister.as_view(), name='register'),
    #path("login/", UserLogin.as_view(), name='login'),
    ]
