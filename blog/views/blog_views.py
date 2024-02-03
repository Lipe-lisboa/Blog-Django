from django.shortcuts import render
from django.core.paginator import Paginator
from blog.models import Page, Post 
from django.db.models import Q



def index (request):
    #posts = Post.objects.order_by('-id').filter(is_published=True)
    posts = Post.objects.get_published()
    paginator = Paginator(posts, 9 )
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    return render( 
        request,
        'blog/pages/index.html',
        {
            'page_obj': page_obj,
        }
    )
    
def author_created (request, author_id):
    #posts = Post.objects.order_by('-id').filter(is_published=True)
    posts = Post.objects.get_published().filter(user_created__id=author_id)
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
def category (request, slug):
    #posts = Post.objects.order_by('-id').filter(is_published=True)
    
    #como a category é uma forenkey do Post, para pegar algum campo
    # de category, eu tenho que utilizar dois anderline
    posts = Post.objects.get_published().filter(category__slug=slug)
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

def tag(request, slug):
        #posts = Post.objects.order_by('-id').filter(is_published=True)
    
    #como a category é uma forenkey do Post, para pegar algum campo
    # de category, eu tenho que utilizar dois anderline
    posts = Post.objects.get_published().filter(tags__slug=slug)
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
    
def search(request):
    search_value = request.GET.get('search', '').strip()
    posts = Post.objects.get_published().filter(
        Q(title__icontains=search_value) |
        Q(excerpt__icontains=search_value) |
        Q(content__icontains=search_value)
    )
    paginator = Paginator(posts, 9)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    return render( 
        request,
        'blog/pages/index.html',
        {
            'page_obj': page_obj,
            'search_value':search_value
        }
    )
    
def page(request, slug):
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


def post(request, slug):

    post = Post.objects.get_published().filter(slug=slug).first()
 
    return render(
        request,
        'blog/pages/post.html',
        {
            'post': post,
        }
    )
def posts(request):

    #posts = Post.objects.all()    
    post = Post.objects.get_published()
    paginator = Paginator(post, 1)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
 
    return render(
        request,
        'blog/pages/posts.html',
        {
            'page_obj': page_obj,
        }
    )