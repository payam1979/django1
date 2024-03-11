from django.shortcuts import render, get_object_or_404

from blog.models import Post

from django.utils import timezone

from blog.models import *
# Create your views here.

     



def blog_view(request, **kwargs):
   
    posts = Post.objects.exclude(published_date__gt=timezone.now()).exclude (status= 0)    
    if kwargs.get('cat_name') != None:
        posts = posts.filter(category__name=kwargs['cat_name'])
    if kwargs.get('author_username') != None:
        posts = posts.filter(author__username=kwargs['author_username'])
    
    
    context = {'posts': posts}
    return render(request, 'blog/blog-home.html', context)



def single_view(request, pid):
    posts = Post.objects.exclude(published_date__gt=timezone.now()).exclude (status= 0)
    post = get_object_or_404(posts,pk=pid)
    post.counted_view +=1
    post.save()
    post1 = list(posts)
    
    
    
    
    for i in range(0,len(post1)):
        if post1[i].id == pid:
            if i == 0:
                previous_post = post1[i+1]
                #print(previous_post.id)
                next_post = post1[0]
                #print(next_post.id) 
            elif i == len(post1)-1:
                next_post = post1[i-1]
                #print(next_post.id)
                previous_post = post1[len(post1)-1]
                #print(previous_post.id)
            else:
                next_post = post1[i-1]
                #print(next_post.id)  
                previous_post = post1[i+1]
                #print(previous_post.id)
                
                
   
            
    #print(next_post, post, previous_post)   
       
   
    
    context = {'post': post,
               'next': next_post,
               'previous': previous_post,}
    
    return render(request, 'blog/blog-single.html', context)


    
        

def test(request):
    #post = Post.objects.get(id=pid)
    #posts = Post.objects.filter(status = 1)
    #post = get_object_or_404(Post,pk=pid)
    #context = {'post': post}
    return render(request, 'blog/test.html')


#def detailed_view(request, pid):
    #   post = get_object_or_404(Post,pk=pid)
    #  post.counted_view +=1
    #  context = {'post': post}
    #  post.save()
    #  return render(request, 'blog/blog-detailed.html',context)
    
def blog_category(request, cat_name):
    posts = Post.objects.exclude(published_date__gt=timezone.now()).exclude (status= 0)
    posts = posts.filter(category__name=cat_name)
    context = {'posts': posts}
    return render(request, 'blog/blog-home.html', context)