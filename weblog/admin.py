from django.contrib import admin
from .models import Article, Category


def make_published(modeladmin,request,queryset):
    queryset.update(status='p')
make_published.short_description="انتشار مقالات انتخاب شده"

def make_draft(modeladmin,request,queryset):
    queryset.update(status='d')
make_draft.short_description="پیش نویس شدن مقالات انتخاب شده"


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('position','title', 'slug','parent', 'status')
    list_filter = (['status'])
    search_fields = ('title','slug')
    prepopulated_fields = {'slug':('title',)} 

admin.site.register(Category, CategoryAdmin) 


class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title','thumbnail_tag', 'slug', 'jpublish','status','category_tostr')
    list_filter = ('publish','status')
    search_fields = ('title','description')
    prepopulated_fields = {'slug':('title',)}
    ordering = ['status','publish']
    actions=[make_published, make_draft]


    def category_tostr(slef,obj): 
        return ", ".join([Category.title for Category in obj.category_published()])
    category_tostr.short_description="دسته بندی"

admin.site.register(Article, ArticleAdmin) 