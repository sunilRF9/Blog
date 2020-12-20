from django.shortcuts import render
from rest_framework.response import Response
from .models import Post
from .serializers import PostSerializer
from rest_framework import generics

class PostList(generics.ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

def index(request):
    post = Post.objects.all()
    #context = {'post': post}
    return render(request, 'index.html')

def content(request):
    #post = Post.objects.filter(id=pid)
    #title = post[0].title
    #post = post[0].content
    #context = {'post': post, 'title': title}
    return render(request, 'blog.html')
