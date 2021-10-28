from django.db import models
from django.utils import timezone
# Create your models here.

class Category(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=100, unique=True)
    status = models.BooleanField(default=True, verbose_name="Show Or Not?")
    position = models.IntegerField()
    
    class Meta:
        ordering = ['position']     

    def __str__(self):
        return self.title
    



class Article(models.Model):
    STATUS_CHOICES = (
        ('d','Draft'),
        ('p','Published')
    )
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=100, unique=True) 
    category = models.ManyToManyField(Category)
    description = models.TextField()
    thumbnail = models.ImageField(upload_to="images")
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updatee = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=1, choices=STATUS_CHOICES)

    def __str__(self):
        return self.title  


   