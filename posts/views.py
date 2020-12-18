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
    context = {'post': post}
    return render(request, 'posts/posts.html', context)

def content(request, pid):
    post = Post.objects.filter(id=pid)
    #print(post[0].content)
    post = post[0].content
    context = {'post': post}
    return render(request, 'posts/content.html', context)
