from typing import Any
from django.contrib import admin
from blog.models import Tag,  Category, Page,Post

# Register your models here.

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = 'id', 'name', 'slug',
    list_display_links = 'name',
    search_fields = 'id', 'name', 'slug',
    list_per_page = 10
    ordering = '-id',
    prepopulated_fields = { #este campo slug é prenchido altomaticamente com o nome da tag
        "slug": ('name',)
    }



@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = 'id', 'name', 'slug',
    list_display_links = 'name',
    search_fields = 'id', 'name', 'slug',
    list_per_page = 10
    ordering = '-id',
    prepopulated_fields = { #este campo slug é prenchido altomaticamente com o nome da tag
        "slug": ('name',)
    }



@admin.register(Page)
class PageAdmin(admin.ModelAdmin):
    list_display = 'id', 'title', 'is_published', 'slug',
    list_display_links = 'title',
    search_fields = 'id', 'title', 'slug',
    list_per_page = 10
    ordering = '-id',
    prepopulated_fields = { #este campo slug é prenchido altomaticamente com o nome da tag
        "slug": ('title',)
    }
    
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):

    list_display = 'id', 'title', 'is_published',  'user_created',
    list_display_links = 'title',
    search_fields = 'id', 'slug', 'title', 'excerpt', 'content',
    list_per_page = 50
    list_filter = 'category', 'is_published',
    list_editable = 'is_published',
    ordering = '-id',
    readonly_fields = (
        'date_Time_created', 'date_Time_updated', 'user_created', 'user_updated',
    
    )
    prepopulated_fields = {
        "slug": ('title',),
    }
    autocomplete_fields = 'tags', 'category',

    #obj : oq esta sendo alterado
    #form: o forme que esta sendo usado
    #change: se o usuario esta alterando algo ou não
    
    def save_model(self, request, obj, form, change):
        
        if change:
            obj.user_updated = request.user
        
        else:
            obj.user_created = request.user

        return super().save_model(request, obj, form, change)
    
    
        
