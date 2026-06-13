from django.shortcuts import render, get_object_or_404
from blog.models import Post
from django.db.models import F
from django.utils import timezone

# Create your views here.
def index_blog(requests, cat_name=None, auth_username=None):
    posts = Post.objects.filter(status=1, published_date__lte=timezone.now()).order_by('-published_date')
    if cat_name:
        posts = posts.filter(category__name=cat_name)
    if auth_username:
        posts = posts.filter(author__username=auth_username)
    context = {'posts': posts}
    return render(requests, "blog/blog-home.html", context)

def single_blog(requests, pid):
    posts = Post.objects.filter(status=1, published_date__lte=timezone.now())
    post = get_object_or_404(posts, pk=pid)

    Post.objects.filter(id=pid).update(counted_views=F('counted_views') + 1)

    previous_post = (
        posts
        .filter(published_date__lt=post.published_date)
        .order_by('-published_date')
        .first()
    )

    next_post = (
        posts
        .filter(published_date__gt=post.published_date)
        .order_by('published_date')
        .first()
    )

    context = {'post': post, 'previous_post': previous_post, 'next_post': next_post}

    post.refresh_from_db()
    return render(requests, "blog/blog-single.html", context=context)

def search_blog(requests):
    posts = Post.objects.filter(status=1, published_date__lte=timezone.now()).order_by('-published_date')
    if requests.method == 'GET':
        if s := requests.GET.get('s'):
            posts = posts.filter(content__contains=s)

    context = {'posts': posts}
    return render(requests, "blog/blog-home.html", context)