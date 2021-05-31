from blog.models import Post
from django import forms
from django.forms.fields import ImageField

class blogForm(forms.ModelForm):
    title = forms.CharField(max_length=100, widget=forms.TextInput(
        attrs={'class': 'block border border-grey-light w-full p-3 rounded mb-4',
               'placeholder': 'Title'
               }))
    text = forms.CharField(widget=forms.Textarea(
        attrs={
            'class': 'block border border-grey-light w-full p-3 rounded mb-8',
            'placeholder': 'Write content of your blog here...'
        }))
    
    class Meta:
        model = Post
        fields = ('title', 'text', 'image')

