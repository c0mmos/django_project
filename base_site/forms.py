from django import forms
from base_site.models import contact, NewsLetter
from captcha.fields import CaptchaField

class ContactForm(forms.ModelForm):
    captcha = CaptchaField()

    class Meta:
        model = contact
        fields = '__all__'


class NewsLetterForm(forms.ModelForm):
    
    class Meta:
        model = NewsLetter
        fields = '__all__'