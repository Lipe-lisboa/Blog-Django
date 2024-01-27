from django.db import models
from utils.validate import valideta_png
from utils.images import resize_image
# Create your models here.


class SiteSetup(models.Model):
    class Meta:
        verbose_name = 'Setup'
        verbose_name_plural = 'Setups'

    
    #configuração do site
    title = models.CharField(max_length=65)
    description = models.CharField(max_length=255)

    show_header = models.BooleanField(default=True)
    show_search = models.BooleanField(default=True)
    show_menu = models.BooleanField(default=True)
    show_description = models.BooleanField(default=True)
    show_pagination = models.BooleanField(default=True)
    show_footer = models.BooleanField(default=True)
    favicon = models.ImageField( #pip install pillow
        blank=True,
        upload_to='assets/%Y/%m/',
        validators= [valideta_png]
        )
    
    def save(self,*args, **kwargs):
        #antes de salvar
        favicon_name_atual = self.favicon.name
        super().save(*args, **kwargs)
        #depois de salvar
        favicon_changed = False
        new_favicon_name = None
        
        if self.favicon:
            new_favicon_name = self.favicon.name
            favicon_changed = bool(favicon_name_atual  != new_favicon_name)
        
        
        print(f'favicon foi alterado? {favicon_changed}')
        if favicon_changed:
            resize_image(self.favicon, 32)
        
        
    def __str__(self):
        return self.title

class MenuLink(models.Model):
    class Meta:
        verbose_name = 'Menu Link'
        verbose_name_plural = 'Menu Links'

    text = models.CharField(max_length=50)
    url_or_path = models.CharField(max_length=2048)
    new_tab = models.BooleanField(default=False)
    
    #relaçaõ de muitos para um. varios likes para um setup
    #MenuLink pertence a SiteSetup, entao o certo é colocar a ForeignKey aqui
    site_setup = models.ForeignKey(
        SiteSetup,
        on_delete=models.CASCADE,
        blank=True,
        null=True,
        default=None,
    )

    def __str__(self):
        return self.text