from django.shortcuts import render
from django.views.generic import ListView , DetailView, CreateView, UpdateView, DeleteView
from .models import *
from django.urls import path, reverse
from .forms import PostForm, UpdateForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.

class Homeview(ListView):
    model= Post
    template_name='index.html'
    ordering='-id'

class Detailedarticle(DetailView):
    model= Post
    template_name='article.html'


class AddPost(CreateView, LoginRequiredMixin):
    
    model=Post
    template_name="add_post.html"
    #fields=('title', 'author', 'body' )
    #fields=__all__
    form_class=PostForm
    
    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.author = self.request.user

        self.object.save()
        return super().form_valid(form) 
    def get_success_url(self):
        # Use reverse to dynamically generate the URL with the book ID
        return reverse('articleview', kwargs={'pk': self.object.pk})
    

class Updatearticlepost(UpdateView):
    model=Post
    template_name="updatepost.html"
    # fields=['title', 'title_tag', 'body',]
    form_class=UpdateForm
    
    def get_success_url(self):
        # Use reverse to dynamically generate the URL with the book ID
        return reverse('articleview', kwargs={'pk': self.object.pk})
class Deletepost(DeleteView):
    model=Post
    template_name="deletepost.html"
    def get_success_url(self):
        # Use reverse to dynamically generate the URL with the book ID
        return reverse('home')

