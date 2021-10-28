from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import Article


# Create your views here.
def home(request):
    #we can connect to model and retrive data and send the result to themplate
    context = {
        # "articles":Article.objects.all
        "articles":Article.objects.filter(status='p').order_by('-publish')
    }
    return render(request, "weblog/home.html", context)

 
 
def detail(request, slug):
    context = {
        "article":Article.objects.get(slug=slug)
    }
    return render(request, "weblog/detail.html", context)  