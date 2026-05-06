from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    """Главная страница Yatube"""
    return HttpResponse("<h1>Добро пожаловать в Yatube!</h1><p>Это главная страница</p>")

def group_posts(request, slug):
    """Страница постов, отфильтрованных по группам"""
    return HttpResponse(f"<h1>Сообщество: {slug}</h1><p>Здесь будут посты этой группы</p>")