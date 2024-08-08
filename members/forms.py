from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import PasswordChangeForm
from django import forms

class CreateUser(UserCreationForm):
    email=forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control'}))
    first_name=forms.CharField(max_length=50,widget=forms.TextInput(attrs={'class':'form-control'}))
    last_name=forms.CharField(max_length=50,widget=forms.TextInput(attrs={'class':'form-control'}))
    class Meta:
        model=User
        fields=('username', 'first_name', 'last_name', 'email', 'password1','password2')

    def __init__(self, *args, **kwargs):
        super(CreateUser,self).__init__( *args, **kwargs)
        self.fields["username"].widget.attrs['class'] = 'form-control'
        self.fields["password1"].widget.attrs['class'] = 'form-control'
        self.fields["password2"].widget.attrs['class'] = 'form-control'

class EditUserForm(UserCreationForm):
    email=forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control'}))
    first_name=forms.CharField(max_length=50,widget=forms.TextInput(attrs={'class':'form-control'}))
    last_name=forms.CharField(max_length=50,widget=forms.TextInput(attrs={'class':'form-control'}))
    username=forms.CharField(max_length=50,widget=forms.TextInput(attrs={'class':'form-control'}))
    class Meta:
        model=User
        fields=('username', 'first_name', 'last_name', 'email', 'password')

    def __init__(self, *args, **kwargs):
        super(EditUserForm,self).__init__( *args, **kwargs)
        
        self.fields["password1"].widget.attrs['class'] = 'form-control'
        self.fields["password2"].widget.attrs['class'] = 'form-control'

class ResetPasswordForm(PasswordChangeForm):
    old_password=forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control'}))
    new_password1=forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control'}))
    new_password2=forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control'}))
    class Meta:
        model=User
        fields=('old_password', 'new_password1', 'new_password2')
        