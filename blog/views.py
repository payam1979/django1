from django.shortcuts import render
from blog .models import Post
from datetime import datetime
import pytz


# Create your views here.

dt_naive = datetime.now()

dt_aware_now = datetime(
    year=dt_naive.year,
    month=dt_naive.month,
    day=dt_naive.day,
    hour=dt_naive.hour,
    minute=dt_naive.minute,
    second=dt_naive.second,
    tzinfo=pytz.UTC
)


def blog_view(request):
    
    posts = Post.objects.exclude(published_date__gt=datetime.now()).exclude (status= 0)
    
            
           
    context = {'posts': posts}
    return render(request, 'blog/blog-home.html', context)

def single_view(request):
    return render(request, 'blog/blog-single.html')

def test(request):
    posts = Post.objects.all()
    #posts = Post.objects.filter(status = 1)
    context = {'posts': posts}
    return render(request, 'blog/test.html', context)


