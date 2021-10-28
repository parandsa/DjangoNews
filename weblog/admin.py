from django.contrib import admin
from .models import Article, Category


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('position','title', 'slug', 'status')
    list_filter = (['status'])
    search_fields = ('title','slug')
    prepopulated_fields = {'slug':('title',)} 

admin.site.register(Category, CategoryAdmin) 


class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'publish','status','category_tostr')
    list_filter = ('publish','status')
    search_fields = ('title','description')
    prepopulated_fields = {'slug':('title',)}
    ordering = ['status','publish']

    def category_tostr(slef,obj):
        return "Categoriesh"

admin.site.register(Article, ArticleAdmin) 