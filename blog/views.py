from django.shortcuts import render, get_object_or_404
from .models import Post
from django.http import HttpResponse

def index(request):
    posts = Post.objects.all().order_by('-fecha_publicacion')
    return render(request, 'blog/index.html', {'posts': posts})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})

