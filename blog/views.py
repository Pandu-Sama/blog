from django.shortcuts import render
from .models import Post
from django.http import HttpResponse

def index(request):
    posts = Post.objects.all().order_by('-fecha_publicacion')
    return render(request, 'blog/index.html', {'posts': posts})


