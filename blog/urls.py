from django.urls import path, include
from blog.views import *

app_name = 'blog'

urlpatterns = [
    path('', index_blog, name='index'),
    path('single', single_blog, name='single')
]
