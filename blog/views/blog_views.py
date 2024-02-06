from typing import Any
from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from blog.models import Page, Post 
from django.db.models import Q
from django.contrib.auth.models import User
from django.http import Http404, HttpRequest, HttpResponse
from django.views.generic import ListView, DetailView

#quando a view não tem muita logica (só pega o valor e passa pro template) ai
#eu uso função

#quando a view precisa de uma logica mais complexa (como foi no projeto agenda
# onde teve que ver se era o metodo get ou post), ou quando se repete muito codigo,
# ai a class é mais recomendada 

class PostListView(ListView):
    model = Post
    template_name = 'blog/pages/index.html'
    context_object_name  = 'posts'
    ordering = '-id',
    paginate_by = 9
    queryset = Post.objects.get_published()
    
    
    #get_context_data serve para alterar o context
    def get_context_data(self, **kwargs):
        
        context = super().get_context_data(**kwargs)
        
        context.update({
            'page_title': 'Home - '
        })
        return context
    
class AuthorCreatedListView(PostListView):
    
    def __init__(self, **kwargs: Any) -> None:
        super().__init__(**kwargs)
        
        self._temp_context = {}

    def get_context_data(self, **kwargs):
        
        context = super().get_context_data(**kwargs)
        
        user = self._temp_context['user']
        
        user_full_name = None
        if user.first_name and user.last_name:
            
            user_full_name = f'{user.first_name} {user.last_name}'
        else:
            user_full_name = user.username
            
        page_title  = 'Posts de ' + user_full_name
        
        context.update({
            'page_title':page_title
        })        
        return context
    
    #get_queryset server para mexer na queryset (filtrar por exemplo) 
    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.filter(
            user_created__id=self._temp_context['user'].id
        )
        return queryset

    #get serve para retornar uma HttpResponse (um erro ou redirecionar para outra pagina
    # por exemplo) 
    def get(self, request: HttpRequest, *args: Any, **kwargs: Any) -> HttpResponse:
        
        # pose ter acesso ao parametro da url por self.kwargs
        author_id  = self.kwargs.get('author_id')
        user = User.objects.filter(id=author_id).first()
        
        if user is None:
            raise Http404()
        
        self._temp_context.update({
            'user':user
        })
        
        return super().get(request, *args, **kwargs)
    
class CategoryListView(PostListView):

    allow_empty = False # allow_empty = False  é igual     if len(page_obj) == 0:
                        #                                       raise Http404
    
    def get_context_data(self, **kwargs) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        
        # posso ter acesso aos objetos (posts) em uma ListView, usando self.object_list[]
        page_title = f'{self.object_list[0].category.name} - category - '
        
        context.update({
            'page_title': page_title
        })
        return context
    
    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.filter(
            category__slug=self.kwargs.get("slug")
        )
        return queryset
 
class TagListView(PostListView):
    
    allow_empty = False
    
    def get_context_data(self, **kwargs) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        page_title  = f'{self.object_list[0].tags.first().name} - tag - '
        context.update({
            'page_title':page_title
        })
        return context
    
    
    def get_queryset(self):
        queryset = super().get_queryset()
        
        queryset  = queryset.filter(
            tags__slug=self.kwargs.get('slug')
        )
        return queryset
    
class SearchListView(PostListView):
    def __init__(self, **kwargs: Any) -> None:
        super().__init__(**kwargs)
        self._search_value = ''
        
    
    # posso usar o metodo setup para ter acesso a request    
    def setup(self, request, *args, **kwargs):
        self._search_value = request.GET.get('search', '').strip()
        return super().setup(request, *args, **kwargs)
        
    def get_queryset(self):
        queryset =  super().get_queryset()
        queryset = queryset.filter(
            Q(title__icontains=self._search_value) |
            Q(excerpt__icontains=self._search_value) |
            Q(content__icontains=self._search_value)
        )
        return queryset
    
    def get_context_data(self, **kwargs) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        
        page_title  = f'{self._search_value[:30]} - Search - '
        context.update({
            'page_title':page_title,
            '_search_value':self._search_value,
        })
        return context
    
    def get(self, request: HttpRequest, *args: Any, **kwargs: Any) -> HttpResponse:
        
        if self._search_value == '':
            return redirect('blog:index')
        return super().get(request, *args, **kwargs)

class PageDetailView(DetailView):
    
    model = Page
    template_name = 'blog/pages/page.html'
    slug_field = 'slug'
    context_object_name = 'page'
     
    def get_queryset(self):
        queryset = super().get_queryset()
        
        queryset = queryset.filter(
            is_published = True
        )
        return queryset
    
    
    def get_context_data(self, **kwargs) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        
        # posso ter acesso ao objeto (page) em uma DetailView, usando self.get_object()
        page_title  = f'{self.get_object().title} - Page - '
        context.update({
            'page_title': page_title
        }) 
        return context

class PostDetailView(DetailView):
    model = Post
    template_name = 'blog/pages/post.html'
    slug_field = 'slug'
    context_object_name = 'post'
    
    
    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.filter(
            is_published = True
        )
        return queryset
    
    def get_context_data(self, **kwargs) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        page_title  = f'{self.get_object().title} - Post - '
        context.update({
            'page_title':page_title 
        })
        return context
    
class PostsListView(PostListView):
    allow_empty = False
    paginate_by = 1
    template_name = 'blog/pages/posts.html'
    
    def get_context_data(self, **kwargs) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        
        page_title  = f'{self.object_list[0].title} - Post - '
        
        context.update({
            'page_title':page_title
        })
        return context
    