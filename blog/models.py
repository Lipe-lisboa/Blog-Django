from django.db import models
from utils.rands import slugify_new
import datetime
from django.contrib.auth.models import User
from utils.images import resize_image
from django_summernote.models import AbstractAttachment


# Create your models here.
class PostAttachment(AbstractAttachment):
    def save(self, *args, **kwargs):
        if not self.name:
            self.name = self.file.name
            
        img_name_atual = self.file.name
        super_save = super().save(*args, **kwargs)

        img_changed = False
        new_img_name = None
        
        if self.file:
            new_img_name = self.file.name
            img_changed = bool(img_name_atual  != new_img_name)
        
        if img_changed:
            resize_image(self.file, 900)
        
        return super_save
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
    
    
class PostManager(models.Manager):
    def get_published(self):
        #self == objects
        return self\
            .filter(is_published=True)\
            .order_by('-id')   

class Post(models.Model):
    class Meta:
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'
    
    objects = PostManager()
    title = models.CharField(max_length=65)

    slug = models.SlugField(
        unique=True, default=None,
        null=True, blank=True, max_length=70,
    )
    
    excerpt =  models.CharField(max_length=150) # um resumo (subtitle)
    
    is_published = models.BooleanField(
        default=False,
        help_text = 'Este campo precisa estar marcado para o post ser exibida publicamente'
        )
    
    content = models.TextField()
    
    cover = models.ImageField(upload_to='posts/%Y/%m/', blank=True)
    cover_in_post_content = models.BooleanField(
        default=True,
        help_text = 'Este campo precisa estar marcado para exibir a capa entro do post',
    )

    #data_now = datetime.date.today()
    #data_create = models.CharField(default=str(datetime.date.strftime(data_now,'%d/%m/%Y')), max_length=225)
    
    #auto_now_add=True gera a data altomaticamente só um vez 
    #auto_now=True gera uma nova dada toda vez que eu salvar o campo 
    date_Time_created = models.DateTimeField(auto_now_add=True)
    date_Time_updated = models.DateTimeField(auto_now=True) 
    
    #user.post_user_created.all
    user_created = models.ForeignKey(
        User, on_delete= models.SET_NULL,
        blank=True, null=True,
        related_name= 'post_created'
        
    )
    
    #user.post_updated.all
    user_updated = models.ForeignKey(
        User, on_delete= models.SET_NULL,
        blank=True, null=True,
        related_name= 'post_updated' 
    )

    #relação de muitos para um. varios posts para uma categoria
    #Posts pertence a Category, entao o certo é colocar a ForeignKey aqui
    category = models.ForeignKey(
        Category, on_delete=models.SET_NULL, null=True, blank=True,
    )
    
    #relação de muitos para muitos. varios posts pode ter varias tags, ou vice e versa
    #Posts pertence a Category, entao o certo é colocar a ForeignKey aqui
    tags = models.ManyToManyField(
        Tag, blank=True, default='',
        related_name= 'tag_post'
    )
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify_new(self.title)
            
        cover_name_atual = self.cover.name
        super_save = super().save(*args, **kwargs)
    
        cover_changed = False
        new_cover_name = None
        
        if self.cover:
            new_cover_name = self.cover.name
            cover_changed = bool(cover_name_atual  != new_cover_name)
        
        
        print(f'cover foi alterado? {cover_changed}')
        if cover_changed:
            resize_image(self.cover, 900)
            
        return super_save
            
    def __str__(self) -> str:
        return self.title








