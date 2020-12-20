from . import views
from django.urls import path

urlpatterns = [
    path('api/', views.PostList.as_view()),
    path('api/<int:pk>/', views.PostDetail.as_view()),
    path('', views.index, name='home'),
    #path('post/<int:pid>', views.content, name='post')
    path('blog/', views.blog, name='post-list'),
    path('search/', views.search, name='search'),
    path('post/<id>/', views.post, name='post-detail')
]
