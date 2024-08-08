from django import forms
from .models import Post, Category
from django.forms import ModelChoiceField



class PostForm(forms.ModelForm):
    category = ModelChoiceField(queryset=Category.objects.all())
    
    class Meta:
        model=Post
        fields=('title','title_tag','category' ,'body',)
        widgets={
            'title':forms.TextInput(attrs={'class':'form-control', 'placeholder':'Name your title'}),
            'title_tag':forms.TextInput(attrs={'class':'form-control', 'placeholder':'Name your title_tag'}),
            'category':forms.Select(attrs={'class':'form-control'}),
            'body':forms.Textarea(attrs={'class':'form-control', 'placeholder':'Enter Text here'}),
        }

class UpdateForm(forms.ModelForm):
    class Meta:
        model=Post
        
        fields=('title','title_tag', 'body',)
        widgets={
            'title':forms.TextInput(attrs={'class':'form-control'}),
            'title_tag':forms.TextInput(attrs={'class':'form-control'}),
            'body':forms.Textarea(attrs={'class':'form-control', }),
        }

class CategoryForm(forms.ModelForm):
    class Meta:
        model=Category
        
        fields=('categry',)
        widgets={
            
            'categry':forms.TextInput(attrs={'class':'form-control'}),
            
        }



