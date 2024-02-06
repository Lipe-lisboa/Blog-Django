

def lower_ip (str:str):
    print(str.lower())
    
lower_ip(('À'))

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

#def author_created (request, author_id):
#    user = User.objects.filter(id=author_id).first()
#    
#    if user is None:
#        raise Http404()
#    posts = Post.objects.get_published().filter(user_created__id=author_id)
#    paginator = Paginator(posts, 9)
#    page_number = request.GET.get("page")
#    page_obj = paginator.get_page(page_number)
#    
#    user_full_name = None
#    if user.first_name and user.last_name:
#        
#        user_full_name = f'{user.first_name} {user.last_name}'
#    else:
#        user_full_name = user.username
#        
#    page_title  = 'Posts de ' + user_full_name
#    return render( 
#        request,
#        'blog/pages/index.html',
#        {
#            'page_obj': page_obj,
#            'page_title': page_title
#        }
#    )


#def category (request, slug):
#    
    #como a category é uma forenkey do Post, para pegar algum campo
    # de category, eu tenho que utilizar dois anderline
#    posts = Post.objects.get_published().filter(category__slug=slug)
#    
#    paginator = Paginator(posts, 9)
#    page_number = request.GET.get("page")
#    page_obj = paginator.get_page(page_number)
#
#    if len(page_obj) == 0:
#        raise Http404
#    
#    page_title  = f'{page_obj[0].category.name} - category - '
#    
#    return render( 
#        request,
#        'blog/pages/index.html',
#        {
#            'page_obj': page_obj,
#            'page_title': page_title,
#        }
#    )


#def tag(request, slug):
        #posts = Post.objects.order_by('-id').filter(is_published=True)
    
    #como a category é uma forenkey do Post, para pegar algum campo
    # de category, eu tenho que utilizar dois anderline
#    posts = Post.objects.get_published().filter(tags__slug=slug)
#    paginator = Paginator(posts, 9)
#    page_number = request.GET.get("page")
#    page_obj = paginator.get_page(page_number)
#    
#    if len(page_obj) == 0:
#        raise Http404
#    
#    page_title  = f'{page_obj[0].tags.first().name} - tag - '
#
#    return render( 
#        request,
#        'blog/pages/index.html',
#        {
#            'page_obj': page_obj,
#            'page_title': page_title 
#        }
#    )
