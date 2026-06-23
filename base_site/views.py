from django.shortcuts import render
from django.http import *
from base_site.forms import ContactForm, NewsLetterForm
from django.contrib import messages


def maintenance(request):
    return HttpResponse("""
    <h1>Website Is Not Deployed Yet</h1>
    <p>Coming Soon...</p>
    """)

def index_home(request):
    return render(request, 'website/index.html')

def index_about(request):
    return render(request, 'website/about.html')

def index_contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            messages.add_message(request, messages.SUCCESS, 'Your Ticket submitted successfully')
            form.save()
        else:
            messages.add_message(request, messages.ERROR, "Your Ticket did not submitted")

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
    
def handler404(request, exception):
    return render(request, 'error_codes/404.html', status=404)

def handler500(request):
    return render(request, 'error_codes/500.html', status=500)