from django.shortcuts import render
from django.http import HttpResponse
from blog.models import Post
from django.utils import timezone

# Create your views here.
def index_home(request):
    posts = Post.objects.filter(status=1, published_date__lte=timezone.now()).order_by('-published_date')

    context =  {'posts': posts[:6]}
    return render(request, 'website/index.html', context=context)

def index_about(request):
    return render(request, 'website/about.html')

def index_contact(request):
    return render(request, 'website/contact.html')