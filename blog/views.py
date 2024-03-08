from django.shortcuts import render, get_object_or_404
from blog .models import Post
from datetime import datetime
import pytz


# Create your views here.




def blog_view(request):
   
    posts = Post.objects.exclude(published_date__gt=datetime.now()).exclude (status= 0)    
    context = {'posts': posts}
    return render(request, 'blog/blog-home.html', context)



def single_view(request, pid):
    post = get_object_or_404(Post,pk=pid)
    post.counted_view +=1
    context = {'post': post}
    post.save()
    return render(request, 'blog/blog-single.html', context)

def test(request, pid):
    #post = Post.objects.get(id=pid)
    #posts = Post.objects.filter(status = 1)
    post = get_object_or_404(Post,pk=pid)
    context = {'post': post}
    return render(request, 'blog/test.html', context)


#def detailed_view(request, pid):
    #   post = get_object_or_404(Post,pk=pid)
    #  post.counted_view +=1
    #  context = {'post': post}
    #  post.save()
    #  return render(request, 'blog/blog-detailed.html',context)
    
