from django.contrib import admin
from django.urls import path
from .views import *
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',Homeview.as_view(),name='home' ),
    path('article/<int:pk>', Detailedarticle.as_view(), name='articleview' ),
    path('add_post/', AddPost.as_view(),name='addpost' ),
    path('updatepost/<int:pk>', Updatearticlepost.as_view(),name='updatepost' ),
     path('deletetepost/<int:pk>', Deletepost.as_view(),name='deletepost' )
]
