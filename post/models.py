from django.db import models
from django.contrib.auth.models import User 
from django.urls import reverse_lazy
from ckeditor.fields import RichTextField

class Category(models.Model):
    categry=models.CharField(max_length=50)

    def __str__(self):
        return self.categry

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=50)
    title_tag=models.CharField(max_length=20, null=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    body = RichTextField(blank=True, null=True)
    post_time=models.TimeField(auto_now_add=True)
    post_date=models.DateField(auto_now_add=True)
    category=models.CharField(max_length=225, default='coding')
    likes=models.ManyToManyField(User, related_name="blog_likes")
    # category=models.ForeignKey(category , default="coding" )
    def __str__(self):
        return self.title+' | '+str(self.author)
    
    def total_likes(self):
        return self.likes.count()
    
    

