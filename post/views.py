from django.shortcuts import render
from django.views.generic import ListView , DetailView, CreateView, UpdateView
from .models import *
from django.urls import path, reverse
from .forms import PostForm
# Create your views here.

class Homeview(ListView):
    model= Post
    template_name='index.html'

class Detailedarticle(DetailView):
    model= Post
    template_name='article.html'

class AddPost(CreateView):
    model=Post
    template_name="add_post.html"
    #fields=('title', 'author', 'body' )
    #fields=__all__
    form_class=PostForm
    def get_success_url(self):
        # Use reverse to dynamically generate the URL with the book ID
        return reverse('articleview', kwargs={'pk': self.object.pk})
class Updatearticlepost(UpdateView):
    model=Post
    template_name="updatepost.html"
    fields=['title', 'title_tag', 'body',]
    def get_success_url(self):
        # Use reverse to dynamically generate the URL with the book ID
        return reverse('articleview', kwargs={'pk': self.object.pk})
