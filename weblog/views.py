from django.core.paginator import Paginator
from django.db.models.base import Model
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, JsonResponse
from .models import Article, Category
from django.views.generic import ListView, DetailView

# Create your views here.
# def home(request, page=1):
#     #we can connect to model and retrive data and send the result to themplate
#     ariticles_list = Article.objects.filter(status='p')
#     pagintor =  Paginator(ariticles_list,6)
#     # page=request.GET.get('page') ###we don't need to this code beacuse we pass the number of page as an argument and change the url
#     articles = pagintor.get_page(page)
#     context = { 
#         "articles": articles,
#         # "articles":Article.objects.all
#         # "articles": Article.objects.filter(status='p'),#.order_by('-publish'),
#         # "category": Category.objects.filter(status=True)
#     }
#     return render(request, "weblog/home.html", context)

##using listviews
class ArticleList(ListView):
    # model = Article    
    # template_name = "weblog/home.html"
    # context_object_name = "articles" 
    queryset =  Article.objects.published()
    paginate_by = 2
 
# def detail(request, slug):
#     context = {
#         "article":get_object_or_404(Article,slug=slug,status='p')
#     }
#     return render(request, "weblog/detail.html", context)  

##using deailview
class ArticleDetail(DetailView):
    def get_object(self):
        slug = self.kwargs.get('slug')
        return get_object_or_404(Article, slug=slug, status='p')


# def category(reguest, slug, page=1):
#     category = get_object_or_404(Category,slug=slug,status=True)
#     articles_list = category.articles.published()
#     pagintor =  Paginator(articles_list,6)
#     articles = pagintor.get_page(page)
#     context={
#         "category": category,
#         "articles": articles
#     }
#     return render(reguest, "weblog/category.html", context)


##using Listview
class CategoryList(ListView):
    paginated = 5
    template_name = 'weblog/category_list.html'

    def get_queryset(self):
        global category
        slug = self.kwargs.get('slug')
        category = get_object_or_404(Category.objects.active(), slug=slug)
        return category.articles.published()
    

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['category'] = category
        return context

