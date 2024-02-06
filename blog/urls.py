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
    path('author_created/<int:author_id>/', views.AuthorCreatedListView.as_view(), name='author_created'),
    path('category/<slug:slug>/', views.CategoryListView.as_view(), name='category'),
    path('tag/<slug:slug>/', views.TagListView.as_view(), name='tag'),
    path('search/', views.search, name='search'),
]  