from blog.models import Post
from django import forms
from tinymce.widgets import TinyMCE


class blogForm(forms.ModelForm):
    title = forms.CharField(max_length=100, widget=forms.TextInput(
        attrs={'class': 'block border border-grey-light w-full p-3 rounded',
               'placeholder': 'Title'
               }))

    text = forms.CharField(widget=TinyMCE(
        attrs={
            'rows': 30,
        }))

    class Meta:
        model = Post
        fields = ('title', 'text', 'image')

