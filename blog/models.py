from django.db import models
from utils.rands import slugify_new
import datetime


# Create your models here.

class Tag(models.Model):
    class Meta:
        verbose_name = 'Tag'
        verbose_name_plural = 'Tags'

    name = models.CharField(max_length=65)
    slug = models.SlugField(
        unique=True, default=None,
        null=True, blank=True, max_length=70,
    )

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify_new(self.name)
        return super().save(*args, **kwargs)

    def __str__(self) -> str:
        return self.name

class Category(models.Model):
    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    name = models.CharField(max_length=65)
    slug = models.SlugField(
        unique=True, default=None,
        null=True, blank=True, max_length=70,
    )

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify_new(self.name)
        return super().save(*args, **kwargs)

    def __str__(self) -> str:
        return self.name


class Page(models.Model):
    
    title = models.CharField(max_length=65)
    is_published = models.BooleanField(
        default=False,
        help_text = 'Este campo precisa estar marcado para a pagina ser exibida publicamente'
        )
    content = models.TextField()
    slug = models.SlugField(
        unique=True, default=None,
        null=True, blank=True, max_length=70,
    )

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify_new(self.title)
        return super().save(*args, **kwargs)
            
    def __str__(self) -> str:
        return self.title
        
        
#class Category(models.Model):
#    class Meta:
#        verbose_name = 'Category'
#        verbose_name_plural = 'Category'
    
#    data_now = datetime.date.today()
    
#    Author_name = models.CharField(max_length=225)
#    data_create = models.CharField(default=str(datetime.date.strftime(data_now,'%d/%m/%Y')), max_length=225)
#    category = models.CharField(max_length=225)

#    def __str__(self) -> str:
#        return self.Author_name


