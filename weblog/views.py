from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, JsonResponse
from .models import Article, Category


# Create your views here.
def home(request):
    #we can connect to model and retrive data and send the result to themplate
    context = {
        # "articles":Article.objects.all
        "articles": Article.objects.filter(status='p'),#.order_by('-publish'),
        # "category": Category.objects.filter(status=True)
    }
    return render(request, "weblog/home.html", context)

 
 
def detail(request, slug):
    context = {
        "article":get_object_or_404(Article,slug=slug,status='p')
    }
    return render(request, "weblog/detail.html", context)  



def category(reguest, slug):
    context={
        "category":get_object_or_404(Category,slug=slug,status=True)
    }
    return render(reguest, "weblog/category.html", context)