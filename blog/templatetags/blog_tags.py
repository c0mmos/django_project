from django import template
from blog.models import Post
from blog.models import Category
from django.utils import timezone

register = template.Library()

@register.simple_tag(name="totalpost")
def function():
    posts = Post.objects.filter(status=1, published_date__lte=timezone.now()).count()
    return posts

@register.filter
def snippets(value,arg=20):
    res = value[:arg]
    return res + '...'

@register.inclusion_tag('blog/latest-posts.html')
def latestposts():
    posts = Post.objects.filter(status=1, published_date__lte=timezone.now()).order_by("-published_date")[:3]
    return {'posts': posts}

@register.inclusion_tag('blog/blog-categories.html')
def postcategories():
    posts = Post.objects.filter(status=1)
    categories = Category.objects.all()
    cat_dict = {}

    for cat in categories:
        cat_dict[cat] = posts.filter(category=cat).count()

    return {'categories': cat_dict}