from django.contrib import admin
from site_setup.models import MenuLink, SiteSetup

# Register your models here.

@admin.register(MenuLink)
class MenuLinkAdmin(admin.ModelAdmin):
    list_display = 'id','text','url_or_path', 
    list_display_links = 'id', 'text', 'url_or_path',
    search_fields = 'id', 'text', 'url_or_path',
    
@admin.register(SiteSetup)
class SiteSetupAdmin(admin.ModelAdmin):
    list_display ='title','description', 
    
    #não permitir o usuario criar mais de um setup
    def has_add_permission(self, request):
        existe_uma_configuracao = bool(SiteSetup.objects.exists())
        return not existe_uma_configuracao
