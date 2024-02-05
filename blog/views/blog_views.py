from django.shortcuts import render
from django.core.paginator import Paginator
from blog.models import Page, Post 
from django.db.models import Q
from django.contrib.auth.models import User
from django.http import Http404
from django.views.generic import ListView

#quando a view não tem muita logica (só pega o valor e passa pro template) ai
#eu uso função

#quando a view precisa de uma logica mais complexa (como foi no projeto agenda
# onde teve que ver se era o metodo get ou post), ou quando se repete muito codigo,
# ai a class é mais recomendada 

#{'paginator': <django.core.paginator.Paginator object at 0x000001628EE2AAB0>, 'page_obj': <Page 1 of 2>, 'is_paginated': True, 'object_list': <QuerySet [<Post: Post 
#do João>, <Post: Post da Maria>]>, 'posts': <QuerySet [<Post: Post do João>, <Post: Post da Maria>]>, 'view': <blog.views.blog_views.PostListView object at 0x000001628EEC2900>}

class PostListView(ListView):
    model = Post
    template_name = 'blog/pages/index.html'
    context_object_name  = 'posts'
    ordering = '-id'
    paginate_by = 2
    queryset = Post.objects.get_published
    
    
#    def get_queryset(self):
#        queryset = super().get_queryset() 
#        
#        queryset = queryset.filter(is_published= True)
#        return queryset
    
    def get_context_data(self, **kwargs):
        
        context = super().get_context_data(**kwargs)
        
        context.update({
            'page_title': 'Home - '
        })
        return context
    
    
    
    
#def index (request):
    #posts = Post.objects.order_by('-id').filter(is_published=True)
#    posts = Post.objects.get_published()
#    paginator = Paginator(posts, 9 )
#    page_number = request.GET.get("page")
#    page_obj = paginator.get_page(page_number)
#
#    return render( 
#        request,
#        'blog/pages/index.html',
#        {
#            'page_obj': page_obj,
#            'page_title': 'home - '
#        }
#    )
    
def author_created (request, author_id):
    user = User.objects.filter(id=author_id).first()
    
    if user is None:
        raise Http404()
    posts = Post.objects.get_published().filter(user_created__id=author_id)
    paginator = Paginator(posts, 9)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    
    user_full_name = None
    if user.first_name and user.last_name:
        
        user_full_name = f'{user.first_name} {user.last_name}'
    else:
        user_full_name = user.username
        
    page_title  = 'Posts de ' + user_full_name
    return render( 
        request,
        'blog/pages/index.html',
        {
            'page_obj': page_obj,
            'page_title': page_title
        }
    )
def category (request, slug):
    
    #como a category é uma forenkey do Post, para pegar algum campo
    # de category, eu tenho que utilizar dois anderline
    posts = Post.objects.get_published().filter(category__slug=slug)
    
    paginator = Paginator(posts, 9)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    if len(page_obj) == 0:
        raise Http404
    
    page_title  = f'{page_obj[0].category.name} - category - '
    
    return render( 
        request,
        'blog/pages/index.html',
        {
            'page_obj': page_obj,
            'page_title': page_title,
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
    
    if len(page_obj) == 0:
        raise Http404
    
    page_title  = f'{page_obj[0].tags.first().name} - tag - '

    return render( 
        request,
        'blog/pages/index.html',
        {
            'page_obj': page_obj,
            'page_title': page_title 
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
    
    
    page_title  = f'{search_value[:30]} - Search - '

    return render( 
        request,
        'blog/pages/index.html',
        {
            'page_obj': page_obj,
            'search_value':search_value,
            'page_title':page_title,
        }
    )
    
def page(request, slug):
    page = Page.objects.get_published().filter(slug=slug).first()


    if not page:
        raise Http404
    page_title  = f'{page.title} - Page - '
    
    return render(
        request,
        'blog/pages/page.html',
        {
            # 'page_obj': page_obj,
            'page':page,
            'page_title':page_title
        }
    )

def post(request, slug):

    post = Post.objects.get_published().filter(slug=slug).first()
    
    if not post:
        raise Http404
    page_title  = f'{post.title} - Post - '
    
    return render(
        request,
        'blog/pages/post.html',
        {
            'post': post,
            'page_title': page_title
        }
    )
def posts(request):

    #posts = Post.objects.all()    
    post = Post.objects.get_published()
    paginator = Paginator(post, 1)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    
    if len(page_obj) == 0:
        raise Http404
    
    page_title  = f'{page_obj[0].title} - Post - '
 
    return render(
        request,
        'blog/pages/posts.html',
        {
            'page_obj': page_obj,
            'page_title':page_title
        }
    )