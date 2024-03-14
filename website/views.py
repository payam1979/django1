from django.shortcuts import render
from website.models import contact
from website.forms import NameForm, contactForm, NewsletterForm
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import messages
# Create your views here.



def index_view(request):
    return render(request, 'website/index.html')

def about_view(request):
    return render(request, 'website/about.html')

def contact_view(request):
    if request.method == 'POST':
        form = contactForm(request.POST)
        if form.is_valid():
            form.instance.name = 'anonymous'
            form.save()
            messages.add_message(request, messages.SUCCESS, 'we got your ticket')
        else:
            messages.add_message(request, messages.ERROR, 'something went wrong')
    form = contactForm()        
    return render(request, 'website/contact.html', {'form':form})

def elements_view(request):
    return render(request, 'website/elements.html')

def newsletter_view(request):
    if request.method == 'POST':
        form = NewsletterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS, 'we got your email')
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    else:
        messages.add_message(request, messages.ERROR, 'something went wrong')  
    

def test(request):
    if request.method == 'POST':
        form = contactForm(request.POST)
        if form.is_valid():
            #name = form.cleaned_data['name']
            #email = form.cleaned_data['email']
            #subject = form.cleaned_data['subject']
            #message = form.cleaned_data['message']
            #print(name, subject, email, message)
            form.save()
            return HttpResponse('done')
        else:
            return HttpResponse('error')
            
        #print(name)
        #email = request.POST.get('email')
        #subject = request.POST.get('subject')
        #message = request.POST.get('message')
        #c = contact()
        #c.name = name
        #c.email = email
        #c.subject = subject
        #c.message = message
        #c.save()
        #print(c)
    form = contactForm()
    return render(request, 'website/test.html', {'form':form})