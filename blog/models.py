from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.urls import reverse
from taggit.managers import TaggableManager

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
    tags =TaggableManager()
    category =models.ManyToManyField(Category)
    counted_view = models.IntegerField(default=0)
    status = models.BooleanField(default=False)
    login_require = models.BooleanField(default=False)
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


    def get_absolute_url(self):
        return reverse("blog:single", kwargs={'pid': self.id})
    
    
class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    email = models.EmailField()
    subject = models.CharField(max_length=255)
    message = models.TextField()
    approved = models.BooleanField(default=False)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['-created_date']
    def __str__(self):
        return self.name