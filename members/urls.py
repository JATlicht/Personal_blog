from django.contrib import admin
from django.urls import path
from django.contrib.auth.views import LogoutView
from .views import *
urlpatterns = [
   path('register/',Register.as_view(), name='register'),
   
   
]
