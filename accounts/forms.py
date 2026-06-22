from django import forms
from captcha.fields import CaptchaField
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class CreateUser(UserCreationForm):
    email = forms.EmailField(required=True, label='email')
    first_name = forms.CharField(max_length=255, required=True, label='first_name')
    last_name = forms.CharField(max_length=255, required=True, label='last_name')

    class Meta:
        model = User
        fields = ("email", 'first_name', 'last_name', "username", "password1", "password2")

    def save(self, commit=True):
        user = super(UserCreationForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        if commit:
            user.save()
        return user
