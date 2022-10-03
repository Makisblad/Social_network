from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path("", test, name='test'),
    #path("register/", UserRegister.as_view(), name='register'),
    #path("login/", UserLogin.as_view(), name='login'),
    ]
