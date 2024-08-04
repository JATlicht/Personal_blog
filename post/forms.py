from django import forms
from .models import Post

class PostForm(forms.ModelForm):
    class Meta:
        model=Post
        
        fields=('title','title_tag', 'body',)
        widgets={
            'title':forms.TextInput(attrs={'class':'form-control', 'placeholder':'Name your title'}),
            'title_tag':forms.TextInput(attrs={'class':'form-control', 'placeholder':'Name your title_tag'}),
            
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