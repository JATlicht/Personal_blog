from django.db.models.base import Model as Model
from django.db.models.query import QuerySet
from django.shortcuts import render, redirect
from django.views import generic
from django.contrib.auth.views import PasswordChangeView
from .forms import EditUserForm
from .forms import CreateUser, ResetPasswordForm
from django.urls import reverse_lazy
from django.contrib.auth import logout

from django.contrib.auth .forms import PasswordChangeForm

class Register(generic.CreateView):
    form_class=CreateUser
    template_name='registration/register.html'
    success_url=reverse_lazy('login')
    

class EditUser(generic.UpdateView):
    form_class=EditUserForm
    template_name='registration/edit_user.html'
    success_url=reverse_lazy('login')
    def get_object(self):
        return self.request.user
    
    

class PasswordReset(PasswordChangeView):
    form_class=ResetPasswordForm
    template_name='registration/resetpassword.html'
    success_url=reverse_lazy('resetsuccess')

def passwordsuccess(request):
    return render(request, 'registration/resetsuccess.html')



