from django.shortcuts import render
from django.core.paginator import Paginator
from blog.models import Page, Post

PER_PAGE = 9

def index (request):
    #posts = Post.objects.order_by('-id').filter(is_published=True)
    posts = Post.objects.get_published()
    paginator = Paginator(posts, PER_PAGE )
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
    
    #paginator = Paginator(posts, 9)
    #page_number = request.GET.get("page")
    #page_obj = paginator.get_page(page_number)

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
    paginator = Paginator(posts, PER_PAGE )
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
 
    return render(
        request,
        'blog/pages/post.html',
        {
            'page_obj': page_obj,
        }
    )