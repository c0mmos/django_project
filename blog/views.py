from django.shortcuts import render
from blog.models import Post

# Create your views here.
def index_blog(requests):
    context = {'posts' : Post.objects.filter(status=1)}
    return render(requests, "blog/blog-home.html", context)

def single_blog(requests):
    return render(requests, "blog/blog-single.html")