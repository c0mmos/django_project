from django.shortcuts import render
from django.http import *
from base_site.forms import ContactForm, NewsLetterForm
from django.contrib import messages

# Create your views here.
def index_home(request):
    return render(request, 'website/index.html')

def index_about(request):
    return render(request, 'website/about.html')

def index_contact(request):
    if request.method == 'POST':
        data = request.POST.copy()
        data['name'] = 'Anonymous'

        form = ContactForm(data)
        if form.is_valid():
            messages.add_message(request, messages.SUCCESS, 'Your ticket submitted successfully')
            form.save()
        else:
            messages.add_message(request, messages.ERROR, "Your ticket did not submitted")

    form = ContactForm()
    return render(request, 'website/contact.html', {'form': form})

def index_newsletter(request):
    if request.method == 'POST':
        form = NewsLetterForm(request.POST)
        if form.is_valid():
            messages.add_message(request, messages.SUCCESS, 'Your ticket submitted successfully')
            form.save()
            return HttpResponseRedirect('/')
        else:
            messages.add_message(request, messages.ERROR, "Your ticket did not submitted")
    else:
        return HttpResponseRedirect('/')