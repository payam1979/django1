from django.shortcuts import render, get_object_or_404

from blog.models import Post

from django.utils import timezone

from blog.models import *

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# Create your views here.

     



def blog_view(request, **kwargs):
   
    posts = Post.objects.exclude(published_date__gt=timezone.now()).exclude (status= 0)    
    if kwargs.get('cat_name') != None:
        posts = posts.filter(category__name=kwargs['cat_name'])
    if kwargs.get('author_username') != None:
        posts = posts.filter(author__username=kwargs['author_username'])
    if kwargs.get('tag_name') != None:
        posts = posts.filter(tags__name__in=[kwargs['tag_name']])
        
    posts = Paginator(posts,3)
    
    try:
        page_number = request.GET.get('page')
        posts = posts.get_page(page_number)
    except PageNotAnInteger:
        posts = posts.get_page(1)  
    except EmptyPage:
        posts = posts.get_page(1)
        
    
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



def test(request, author_name=None):
    #post = Post.objects.get(id=pid)
    #posts = Post.objects.filter(status = 1)
    #post = get_object_or_404(Post,pk=pid)
    #context = {'post': post}
    posts = Post.objects.exclude(published_date__gt=timezone.now()).exclude (status= 0)
    if author_name != None:
        posts = posts.filter(author__first_name=author_name)
    context = {'posts': posts}
    return render(request, 'blog/test.html', context)


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


def blog_search(request):
    posts = Post.objects.exclude(published_date__gt=timezone.now()).exclude (status= 0)
    if request.method == 'GET':
        if s:= request.GET.get('s'):
            posts = posts.filter(content__contains=s)
     
    
    context = {'posts': posts}
    return render(request, 'blog/blog-home.html', context)