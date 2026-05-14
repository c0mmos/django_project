from django.urls import path, include
from base_site.views import *

urlpatterns = [
    path('', index_home),
    path('contact', index_contact),
    path('about', index_about),
    path('elements', index_elements)
]
