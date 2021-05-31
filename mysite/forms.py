from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class signupForm(UserCreationForm):
    username = forms.CharField(max_length=100, widget=forms.TextInput(
        attrs={'class': 'block border border-grey-light w-full p-3 rounded mb-4',
                'placeholder': 'Username'
        }))
    password1 = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'block border border-grey-light w-full p-3 rounded mb-4',
                'placeholder': 'Password',
                'type': 'password'
        }))
    password2 = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'block border border-grey-light w-full p-3 rounded mb-4',
                'placeholder': 'Confirm password',
                'type': 'password'
        }))


class loginForm(forms.Form):
    username = forms.CharField(max_length=100, widget=forms.TextInput(
    attrs={'class': 'block border border-grey-light w-full p-3 rounded mb-4',
            'placeholder': 'Username'
    }))
    password = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'block border border-grey-light w-full p-3 rounded mb-4',
                'placeholder': 'Password',
                'type': 'password'
        }))
