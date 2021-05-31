from django.http.response import HttpResponse
from django.contrib import messages
from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from .models import Post
from .forms import blogForm

# Create your views here.


def index(request):
    active = "blog-index"
    posts = Post.objects.all().order_by("-id")[:3]
    return render(request, 'blog/index.html', {'posts': posts, 'active': active})


def blogList(request):
    posts = Post.objects.all()
    return render(request, 'blog/blog-list.html', {'posts': posts})


def blogDetail(request, id):
    post = Post.objects.get(id=id)
    return render(request, 'blog/blog-detail.html', {'post': post})


def blogCreate(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = blogForm(request.POST, request.FILES)
            if form.is_valid():
                post = form.save(commit=False)
                post.author = User.objects.get(id=request.user.id)
                print(post)
                post.save()
                messages.success(request, "Post created")
                return redirect('blogs.index')
        else:
            form = blogForm()
        return render(request, 'blog/blog-form.html', {'form': form})
    else:
        return HttpResponse("Not allowed!!!")
