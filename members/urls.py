from django.contrib import admin
from django.urls import path
from django.contrib.auth.views import LogoutView
from .views import *
urlpatterns = [
   path('register/',Register.as_view(), name='register'),
   path('EditUser/',EditUser.as_view(), name='edituser'),
   path('resetpassword', PasswordReset.as_view(),name='resetpassword'),
   path( 'success',passwordsuccess, name='resetsuccess')
   
]
