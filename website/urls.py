from django.urls import path
from website.views import *



urlpatterns = [
    
   
    path('', website.index_view),
    path('about', website.about_view),
    path('contact', website.contact_view),
    path('elements', website.elements_view),
]
