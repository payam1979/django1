from django.shortcuts import render

# Create your views here.

app_name = 'blog'

def index_view(request):
    return render(request, 'blog/blog-home.html')

def single_view(request):
    return render(request, 'blog/blog-single.html')


