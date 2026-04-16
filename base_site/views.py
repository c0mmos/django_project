from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index_home(request):
    return render(request, 'home.html')

def index_about(request):
    return render(request, 'about.html')

def index_contact(request):
    return render(request, 'contact.html')