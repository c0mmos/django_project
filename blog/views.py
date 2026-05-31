from django.shortcuts import render, get_object_or_404
from blog.models import Post
from datetime import datetime
from django.db.models import F

# Create your views here.
def index_blog(requests):
    context = {'posts' : Post.objects.filter(status=1).exclude(published_date__gt=datetime.now())}
    return render(requests, "blog/blog-home.html", context)

def single_blog(requests, pid):
    posts = Post.objects.filter(status=1).exclude(published_date__gt=datetime.now())
    post = get_object_or_404(posts, pk=pid)
    context = {'post': post}

    Post.objects.filter(id=pid).update(counted_views=F('counted_views') + 1)

    post.refresh_from_db()
    return render(requests, "blog/blog-single.html", context=context)