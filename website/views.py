from django.shortcuts import render

# Create your views here.

app_name = 'website'

def index_view(request):
    return render(request, 'website/index.html')

def about_view(request):
    return render(request, 'website/about.html')

def contact_view(request):
    return render(request, 'website/contact.html')

def elements_view(request):
    return render(request, 'website/elements.html')