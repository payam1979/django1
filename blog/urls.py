from django.urls import path
from blog.views import *



urlpatterns = [
    
   
    path('blog', index_view),
    path('blog/single', single_view),
]

