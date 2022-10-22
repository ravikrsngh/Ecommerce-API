from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.views.decorators.cache import never_cache

index = never_cache(TemplateView.as_view(template_name='index.html'))
