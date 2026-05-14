from django.shortcuts import render

# Create your views here.
def index_blog(requests):
    return render(requests, "blog/blog-home.html")

def single_blog(requests):
    return render(requests, "blog/blog-single.html")