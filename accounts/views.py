from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from accounts.forms import CreateUser
from django.contrib.auth.models import User
from .models import PasswordResetCode
import secrets
from django.core.mail import send_mail

# Create your views here.

def login_view(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            data = request.POST
            username = data['username']
            password = data['password']
            try:
                user = User.objects.get(email=username)
            except User.DoesNotExist:
                try:
                    user = User.objects.get(username=username)
                except User.DoesNotExist:
                    messages.add_message(request, messages.ERROR, 'Login failed please check your username and password and try again')
                    return redirect('/')
            if user.check_password(password):
                user_login = authenticate(request, username=user.username, password=password)
                if user_login is not None:
                    login(request, user_login)
                    messages.add_message(request, messages.SUCCESS, 'You logged in successfully welcome')
                    return redirect('/')
                else:
                    messages.add_message(request, messages.ERROR, 'This username and password does not exist')
                    return redirect('/')
                
            else:
                messages.add_message(request, messages.ERROR, 'Login failed please check your username and password and try again')
                return redirect('/')

        form = AuthenticationForm()
        return render(request, 'accounts/login.html', {'form': form})
    
    else:
        messages.add_message(request, messages.INFO, 'You are already logged in')
        return redirect('/')

@login_required(login_url='/accounts/login')
def logout_view(request):
    logout(request)
    messages.add_message(request, messages.INFO, 'You logged out')
    return redirect('/')

def signup_view(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            form = CreateUser(request.POST)
            if form.is_valid():
                form.save()
                messages.add_message(request, messages.SUCCESS, 'Successfully created the user')
                return redirect('/accounts/login')
            
            else:
                messages.add_message(request, messages.ERROR, 'Sign up failed')
                return redirect('/')
        
        form = CreateUser()
        return render(request, 'accounts/signup.html', {'form': form})
    
    else:
        messages.add_message(request, messages.INFO, 'You are already logged in')
        return redirect('/')
    
def forgot_password(request):
    if request.method == 'POST':
        email = request.POST.get('email')

        try:
            user = User.objects.get(email=email)
        except User.DoesNotExist:
            messages.add_message(request, messages.ERROR, 'User with this email does not exist')
            return redirect('/')

        code = str(secrets.randbelow(900000) + 100000)

        reset_obj, created = PasswordResetCode.objects.get_or_create(
            user=user
        )

        reset_obj.code = code
        reset_obj.save()

        send_mail(
            'Password Reset',
            f'Your reset code is: {code}',
            'Travelista@google.com',
            [user.email],
        )

        request.session['reset_user_id'] = user.id
        request.session['reset_pending'] = True

        return redirect('/accounts/verify-code') 
    
    return render(request, 'accounts/forgot-password.html')

def verify_code(request):
    if not request.session.get('reset_pending'):
        messages.add_message(request, messages.ERROR, 'Invalid password reset session')
        return redirect('/')
    
    if request.method == 'POST':
        entered_code = request.POST.get('code')
        user_id = request.session.get('reset_user_id')

        try:
            reset_obj = PasswordResetCode.objects.get(user_id=user_id)

            if reset_obj.code == entered_code:
                messages.add_message(request, messages.SUCCESS, 'The entered code was correct continue the progress')
                request.session['reset_verified'] = True
                return redirect('/accounts/reset-password')
            
        except PasswordResetCode.DoesNotExist:
            messages.add_message(request, messages.ERROR, 'Invalid code')
            return redirect('/')
    return render(request, 'accounts/verify-code.html')

def reset_password(request):
    if not request.session.get('reset_verified'):
        messages.add_message(request, messages.ERROR, 'Invalid password reset session')
        return redirect('/')
    
    if request.method == 'POST':
        password = request.POST.get('password')
        user = User.objects.get(id=request.session.get('reset_user_id'))

        user.set_password(password)
        user.save()

        request.session.pop('reset_pending', None)
        request.session.pop('reset_verified', None)
        request.session.pop('reset_user_id', None)

        PasswordResetCode.objects.filter(user=user).delete()

        messages.add_message(request, messages.SUCCESS, 'Password change was successful')
        return redirect('/accounts/login')
    
    return render(request, 'accounts/reset-password.html')