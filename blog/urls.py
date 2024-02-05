from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from blog import views

app_name = 'blog'

urlpatterns = [
    path('', views.PostListView.as_view(), name='index'),
    
    #page url
    path('page/<slug:slug>/', views.page, name='page'),
    
    # post url
    path('post/<slug:slug>/', views.post, name='post'),
    path('posts/', views.posts, name='posts'),
    
    # links url 
    path('author_created/<int:author_id>/', views.author_created, name='author_created'),
    path('category/<slug:slug>/', views.category, name='category'),
    path('tag/<slug:slug>/', views.tag, name='tag'),
    path('search/', views.search, name='search'),
]  