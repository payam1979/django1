from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from django.urls import reverse
from django.http import HttpResponseRedirect
# Create your views here.

def login_view(request):
    #if request.user.is_authenticated:
     #   msg = f'You are already logged in as {request.user.username}'
    #else:
     #   msg = 'You are not  logged in'
    #return render(request, 'accounts/login.html', {'msg': msg})
    
    
    
    if not request.user.is_authenticated:
        if request.method == 'POST':
            form = AuthenticationForm(request=request, data=request.POST)
            if form.is_valid():
                username = form.cleaned_data.get('username')
                password = form.cleaned_data.get('password')
                
            #username = request.POST.get('username')
            #password = request.POST.get('password')
                user = authenticate(request, username=username, password=password)
                if user is not None:
                    login(request, user)
                    return redirect('/')
        form = AuthenticationForm()
        context = {'form':form}
        return render(request, 'accounts/login.html', context)
    else:
        return redirect('/')
        





def logout_view(request):
    if request.user.is_authenticated:
        logout(request)
        return redirect('/')
    else:
        return HttpResponseRedirect(reverse('accounts:login'))

def signup_view(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            form = UserCreationForm(request.POST)
            if form.is_valid():
                form.save()
                
                return redirect('/')
        form = UserCreationForm()
        context = {'form':form}    
        return render(request, 'accounts/signup.html', context)
    else:
        return redirect('/')