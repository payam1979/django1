from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=255)
    
    def __str__(self):
        return self.name
    
    
class Post(models.Model):
    image = models.ImageField(upload_to = 'blog/', default='blog/default.jpg')
    image_size = models.ImageField(upload_to = 'blog/', default='blog/next.jpg')
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    title = models.CharField(max_length=255)
    content = models.TextField()
    #tag
    category =models.ManyToManyField(Category)
    counted_view = models.IntegerField(default=0)
    status = models.BooleanField(default=False)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    published_date = models.DateTimeField(null=True)
    
    class Meta:
        ordering = ['-published_date']
        #indexes = [models.Index(fields=['published_date'])]
        #verbose_name = 'پست'
        #verbose_name_plural = 'پست ها'
        
    def __str__(self):
        return self.title

   
