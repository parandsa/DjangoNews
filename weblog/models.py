from django.db import models
from django.db.models.deletion import CASCADE, SET_NULL
from django.utils import timezone
from extensions.utils import jalali_convertor
from django.utils.html import format_html
#Managers
class ArticleManager(models.Manager):
    def published(self):
        return self.filter(status='p')

class CategoryManager(models.Manager):
    def active(self):
        return self.filter(status=True)
# Create your models here.

class Category(models.Model):
    parent = models.ForeignKey('self', default=None, null=True, blank=True, on_delete=SET_NULL, related_name="childeren", verbose_name="زیر  گروه") #this is his own parent
    title = models.CharField(max_length=200,  verbose_name="عنوان")
    slug = models.SlugField(max_length=100, unique=True, verbose_name="آدرس مقاله")
    status = models.BooleanField(default=True, verbose_name="آیا نمایش داده شود؟")
    position = models.IntegerField(verbose_name="پوزیشن")
    
    class Meta:
        verbose_name = "دسته بندی" 
        verbose_name_plural = "دسته بندی ها"
        ordering = ['parent__id', 'position']     

    def __str__(self):
        return self.title
    
    objects = CategoryManager()
    



class Article(models.Model):
    STATUS_CHOICES = (
        ('d','پیش نویس'),
        ('p','منتشر شده')
    )
    title = models.CharField(max_length=200, verbose_name="عنوان")
    slug = models.SlugField(max_length=100, unique=True, verbose_name="آدرس مقاله") 
    category = models.ManyToManyField(Category, verbose_name="دسته بندی", related_name="articles")
    description = models.TextField( verbose_name="توضیحات")
    thumbnail = models.ImageField(upload_to="images", verbose_name="تصویر")
    publish = models.DateTimeField(default=timezone.now, verbose_name="زمان انتشار")
    created = models.DateTimeField(auto_now_add=True)
    updatee = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=1, choices=STATUS_CHOICES, verbose_name="وضعیت")

    def __str__(self):
        return self.title 

    def jpublish(self):
        return  jalali_convertor(self.publish)


    class Meta:
        verbose_name = "مقاله" 
        verbose_name_plural = "مقالات" 
        ordering=['-publish']
        
    jpublish.short_description = "زمان انتشار"


    def thumbnail_tag(self):
        return format_html("<img width=40 height=50 style='border-radius: 5px' src='{}'>".format(self.thumbnail.url))
    thumbnail_tag=short_description="تصویر مقاله"

    def category_published(self):
        return self.category.filter(status=True)
    
    objects= ArticleManager()


   