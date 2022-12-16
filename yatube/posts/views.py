from django.shortcuts import render
from django.http import HttpResponse


# Главная страница
def index(request):
    return HttpResponse('Main list')


# Страница со списком мороженого
def group_posts(request, slug):
    return HttpResponse(f'Group posts listing {slug}')
