from django.contrib import admin
from .models import Post
from django import forms
from tinymce.widgets import TinyMCE


# Register your models here.

class PostAdminForm(forms.ModelForm):
    text = forms.CharField(widget=TinyMCE(attrs={'cols': 80, 'rows': 30}))
    class Meta:
        model = Post
        fields = '__all__'


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_date', 'published_date', 'author')
    list_filter = ('title', 'created_date', 'published_date')
    search_fields = ('title',)
    form = PostAdminForm