from django.contrib import auth
from django.contrib.auth import login, authenticate, logout
from django.core.mail import send_mail
from django.conf import settings
from django.http.response import HttpResponse
from django.shortcuts import render, redirect
from .forms import loginForm, signupForm

def index(request):
        active = "index"
        return render(request, 'index.html', {'active': active})

def signup(request):
    if request.method == 'POST':
        form = signupForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            if user is not None:
                login(request, user)

                # # Send email to the new user
                # subject = 'Welcome to our site'
                # message = 'Thank you for registering!!'
                # email_from = settings.EMAIL_HOST_USER
                # recipient_list = ['kimom20368@revutap.com',]    
                # send_mail( subject, message, email_from, recipient_list )

                return redirect('index')
    else:
        form = signupForm()
    return render(request, 'signup.html', {'form': form})

def signin(request):
    if request.method == 'POST':
        form = loginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=raw_password)
            if user is not None:
                login(request, user)
                return redirect('index')
    else:
        form = loginForm()
    return render(request, 'login.html', {'form': form})

def signout(request):
        logout(request)
        return redirect('index')