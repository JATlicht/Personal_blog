
from django.shortcuts import render, get_object_or_404, HttpResponseRedirect
from django.views.generic import ListView , DetailView, CreateView, UpdateView, DeleteView
from .models import *
from django.urls import path, reverse
from .forms import PostForm, UpdateForm, CategoryForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.

class Homeview(ListView):
    model= Post
    template_name='index.html'
    ordering='-id'
    def get_context_data(self, *args, **kwargs):
        cat_menu=Category.objects.all()
        context=super(Homeview, self).get_context_data( *args, **kwargs)
        context["cat_menu"]=cat_menu
        return context

def likepost(request, pk):
    post=get_object_or_404(Post, id=request.POST.get('post_like'))
    like=False
    if post.likes.filter(id=request.user.id).exists():
        post.likes.remove(request.user)
        like=False
    else :
        post.likes.add(request.user)
        like=True
    return HttpResponseRedirect(reverse('articleview' , args=[str(pk)]))

def sortbycategory(request, cat):
    category_objects=Post.objects.filter(category=cat.replace('-',' '))
    return render(request, 'sortbycategory.html', {'cats':cat.title().replace('-',' '), 'category_objects':category_objects,})

class Detailedarticle(DetailView):
    model= Post
    template_name='article.html'
    def get_context_data(self, *args, **kwargs):
        cat_menu=Category.objects.all()
        obj=get_object_or_404(Post, id=self.kwargs["pk"])
        total_likes=obj.total_likes()
        liked=False
        if obj.likes.filter(id=self.request.user.id).exists():
            liked=True
        context=super(Detailedarticle, self).get_context_data( *args, **kwargs)
        context["cat_menu"]=cat_menu
        context["total_likes"]=total_likes
        context["liked"]=liked
        return context


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

class AddCategory(CreateView):
    
    model=Category
    template_name="add_category.html"
    #fields=('title', 'author', 'body' )
    #fields=__all__
    form_class=CategoryForm
    def get_success_url(self):
        
        return reverse('addpost')

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

