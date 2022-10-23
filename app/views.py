from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.views.decorators.cache import never_cache

def index(request):
    return render(request,'index.html',{})

def indexpk(request,pk):
    return render(request,'index.html',{})
