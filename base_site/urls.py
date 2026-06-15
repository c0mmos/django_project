from django.urls import path, include
from base_site.views import *

app_name = 'website'

urlpatterns = [
    path('', index_home, name='index'),
    path('contact', index_contact, name='contact'),
    path('about', index_about, name='about')
]
