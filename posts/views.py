from django.shortcuts import render, get_object_or_404, redirect
from django.db.models import Count, Q
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .models import Post
from .serializers import PostSerializer
from rest_framework import generics
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.conf import settings
from django.core.cache.backends.base import DEFAULT_TIMEOUT
from django.views.decorators.cache import cache_page

CACHE_TTL = getattr(settings, 'CACHE_TTL', DEFAULT_TIMEOUT)

class PostList(generics.ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class PostDetail(generics.RetrieveUpdateDestroyAPIView):

    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]

    queryset = Post.objects.all()
    serializer_class = PostSerializer

@cache_page(CACHE_TTL)
def index(request):
    post = Post.objects.filter(featured=True)
    latest = Post.objects.order_by('-date_posted')[:3]
    context = {'post': post,
            'latest': latest}
    return render(request, 'index.html', context)

@cache_page(CACHE_TTL)
def blog(request):
    cat_count = category_count()
    print(cat_count)
    recent = Post.objects.order_by('-date_posted')[:3]
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

    context = {'queryset': paginated_qs, 'page_req_var': page_req_var, 'recent':recent, 'cat_count':cat_count}
    return render(request, 'blog.html', context)

@cache_page(CACHE_TTL)
def post(request, slug_text):
    cat_count = category_count()
    print(cat_count)
    recent = Post.objects.order_by('-date_posted')[:3]
    post = Post.objects.filter(slug = slug_text)
    if post.exists():
        post = post.first()
    else:
        return HttpResponse('<h1> Page not found </h1>')
    context = {'post':post, 'recent':recent, 'cat_count':cat_count}
    return render(request, 'post.html', context)

def category_count():
    qs = Post.objects.values('category__title').annotate(Count('category__title'))
    return qs

def search(request):
    qs = Post.objects.all()
    query = request.GET.get('q')
    if query:
        qs = qs.filter(
                Q(title__icontains=query) |
                Q(overview__icontains=query)
                ).distinct()
        context = {'queryset':qs}
        return render(request, 'search_results.html', context)
    else:
        return render(request, 'index.html')
