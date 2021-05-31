from django.shortcuts import render
from .models import Post

# Create your views here.
def index(request):
        active = "blog-index";
        posts = Post.objects.all().order_by("-id")[:3]
        return render(request, 'blog/index.html', {'posts': posts, 'active': active})

def blogList(request):
        posts = Post.objects.all()
        return render(request, 'blog/blog-list.html', {'posts':posts})

def blogDetail(request, id):
        post = Post.objects.get(id=id)
        return render(request, 'blog/blog-detail.html', {'post':post})