from django.shortcuts import render
from rest_framework.response import Response
from .models import Post
from .serializers import PostSerializer
from rest_framework import generics
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

class PostList(generics.ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

def index(request):
    post = Post.objects.filter(featured=True)
    latest = Post.objects.order_by('-date_posted')[:3]
    context = {'post': post,
            'latest': latest}
    return render(request, 'index.html', context)

def blog(request):
    post_list = Post.objects.all()
    paginator = Paginator(post_list, 4)
    page_req_var = 'page'
    page = request.GET.get(page_req_var)
    try:
        paginated_qs = paginator.page(page)
    except PageNotAnInteger:
        paginated_qs = paginator.page(1)
    except EmptyPage:
        paginated_qs = paginator.page(paginator.num_pages)

    context = {'queryset': paginated_qs, 'page_req_var': page_req_var}
    return render(request, 'blog.html', context)

def post(request):
    return render(request, 'post.html')
