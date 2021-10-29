from django.db import models
from django.utils import timezone
from extensions.utils import jalali_convertor
# Create your models here.

class Category(models.Model):
    title = models.CharField(max_length=200,  verbose_name="عنوان")
    slug = models.SlugField(max_length=100, unique=True, verbose_name="آدرس مقاله")
    status = models.BooleanField(default=True, verbose_name="آیا نمایش داده شود؟")
    position = models.IntegerField(verbose_name="پوزیشن")
    
    class Meta:
        verbose_name = "دسته بندی" 
        verbose_name_plural = "دسته بندی ها"
        ordering = ['position']     

    def __str__(self):
        return self.title
    



class Article(models.Model):
    STATUS_CHOICES = (
        ('d','پیش نویس'),
        ('p','منتشر شده')
    )
    title = models.CharField(max_length=200, verbose_name="عنوان")
    slug = models.SlugField(max_length=100, unique=True, verbose_name="آدرس مقاله") 
    category = models.ManyToManyField(Category, verbose_name="دسته بندی")
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
    jpublish.short_description = "زمان انتشار"
    


   