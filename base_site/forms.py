from django import forms
from base_site.models import contact, NewsLetter

class ContactForm(forms.ModelForm):
    # subject = forms.CharField(max_length=255, required=False)

    class Meta:
        model = contact
        fields = '__all__'


class NewsLetterForm(forms.ModelForm):
    
    class Meta:
        model = NewsLetter
        fields = '__all__'