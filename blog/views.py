from django.shortcuts import render, get_object_or_404
from blog.models import Post, Comment
from django.db.models import F
from django.utils import timezone
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from blog.forms import CommentForm
from django.contrib import messages

# Create your views here.
def index_blog(requests, cat_name=None, auth_username=None, tag_name=None):
    posts = Post.objects.filter(status=1, published_date__lte=timezone.now()).order_by('-published_date')
    if cat_name:
        posts = posts.filter(category__name=cat_name)
    if auth_username:
        posts = posts.filter(author__username=auth_username)
    if tag_name:
            posts = posts.filter(tag__name__in=[tag_name])
    posts = Paginator(posts, 2)
    try:
        page_number = requests.GET.get('page')
        posts = posts.get_page(page_number)
    except PageNotAnInteger:
        posts = posts.get_page(1)
    except EmptyPage:
        posts = posts.get_page(1)
        
    context = {'posts': posts}
    return render(requests, "blog/blog-home.html", context)

def single_blog(requests, pid):
    if requests.method == 'POST':
        form = CommentForm(requests.POST)
        if form.is_valid():
            messages.add_message(requests, messages.SUCCESS, 'Your Comment submitted successfully')
            form.save()
        else:
            messages.add_message(requests, messages.ERROR, "Your Comment did not submitted")
    posts = Post.objects.filter(status=1, published_date__lte=timezone.now())
    post = get_object_or_404(posts, pk=pid)
    comments = Comment.objects.filter(approved=True, post=post.id).order_by("-created_date")

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

    form = CommentForm()

    context = {'post': post, 'previous_post': previous_post, 'next_post': next_post, 'comments': comments, 'form': form}

    post.refresh_from_db()
    return render(requests, "blog/blog-single.html", context=context)

def search_blog(requests):
    posts = Post.objects.filter(status=1, published_date__lte=timezone.now()).order_by('-published_date')
    if requests.method == 'GET':
        if s := requests.GET.get('s'):
            posts = posts.filter(content__contains=s)

    context = {'posts': posts}
    return render(requests, "blog/blog-home.html", context)