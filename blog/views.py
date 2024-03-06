from django.shortcuts import render
from blog .models import Post

# Create your views here.



def blog_view(request):
    return render(request, 'blog/blog-home.html')

def single_view(request):
    return render(request, 'blog/blog-single.html')

def test(request):
    #posts = Post.objects.all()
    posts = Post.objects.filter(status = 1)
    context = {'posts': posts}
    return render(request, 'blog/test.html', context)


