from django.shortcuts import render
from django.http import HttpResponse
from blog.models import Post
from django.utils import timezone

# Create your views here.
def index_home(request):
    return render(request, 'website/index.html')

def index_about(request):
    return render(request, 'website/about.html')

def index_contact(request):
    return render(request, 'website/contact.html')