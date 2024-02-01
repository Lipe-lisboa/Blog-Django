from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from blog import views

app_name = 'blog'

urlpatterns = [
    path('', views.index, name='index'),
    path('page/', views.page, name='page'),
    path('post/<slug:slug>/', views.post, name='post'),
]