from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('', Users.as_view(), name='test'),
    #path("/<str:slug>", user, name='test'),
    path("register/", register, name='register'),
    path("login/", user_login, name='login'),
    path("logout/", user_logout, name='logout'),
    ]
