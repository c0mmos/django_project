from django.urls import path, include
from blog.views import *

app_name = 'blog'

urlpatterns = [
    path('', index_blog, name='index'),
    path('<int:pid>', single_blog, name='single'),
    path('category/<str:cat_name>', index_blog, name='category'),
    path('tag/<str:tag_name>', index_blog, name='tags'),
    path('author/<str:auth_username>', index_blog, name='author'),
    path('search/', search_blog, name='search')
]
