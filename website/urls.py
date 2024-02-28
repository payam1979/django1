from django.urls import path
from website.views import *

app_name = 'website'

urlpatterns = [
    
   
    path('', index_view, name='indwx'),
    path('about', about_view, name='about'),
    path('contact', contact_view, name='contact'),
    path('elements', elements_view, name='elements'),
   ]
