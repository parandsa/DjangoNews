from django.urls import path
from django.urls.resolvers import URLPattern 
from .views import home, detail

app_name = 'weblog'
urlpatterns = [
    path('',home, name="home"), 
    path('article/<slug:slug>', detail, name="detail"),  
]