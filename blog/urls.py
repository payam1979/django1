from django.urls import path
from blog.views import *
from blog.feeds import BlogPostFeed
app_name = 'blog'

urlpatterns = [
    
   
    path('', blog_view, name='index'),
    path('single/<int:pid>', single_view, name='single'),
    path('category/<str:cat_name>', blog_view, name='category'),
    path('tag/<str:tag_name>', blog_view, name='tag'),
    path('author/<str:author_username>', blog_view, name='author'),
    path('search/', blog_search, name='search'),
    path('test/<str:author_name>', test, name='test'),
    path('rss/feed', BlogPostFeed()),
    #  path('detailed/<int:pid>', detailed_view, name='detailed'),
    
    
]

