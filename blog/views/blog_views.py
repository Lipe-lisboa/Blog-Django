from django.shortcuts import render
from django.core.paginator import Paginator
from blog.models import Page, Post

posts = list(range(1000))

def index (request):
    
    paginator = Paginator(posts, 9)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    return render(
        request,
        'blog/pages/index.html',
        {
            'page_obj': page_obj,
        }
    )

def page(request):
    page = Page.objects.all()
    paginator = Paginator(posts, 9)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    return render(
        request,
        'blog/pages/page.html',
        {
            # 'page_obj': page_obj,
            'page':page
        }
    )


def post(request):
    
    posts = Post.objects.all()
    paginator = Paginator(posts, 9)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    return render(
        request,
        'blog/pages/post.html',
        {
            # 'page_obj': page_obj,
            'posts':posts
        }
    )