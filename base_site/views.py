from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index_home(requirement):
    return HttpResponse("<h1>Home Page</h1>")

def index_about(requirement):
    return HttpResponse("<h1>About Page</h1>")

def index_contact(requirement):
    return HttpResponse("<h1>Contact Page</h1>")