from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseNotFound, Http404
from .models import *

# Create your views here.


menu = [{'title': 'О сайтe', 'url_name': 'about'},
        {'title': 'Добавить статью', 'url_name': 'add_page'},
        {'title': 'Обратная связь', 'url_name': 'contact'},
        {'title': 'Войти', 'url_name': 'login'}]


def index(request):
    posts = Women.objects.all()
    context = {
        'posts': posts,
        'menu': menu,
        'title': 'Главная страница'
    }
    return render(request, 'women/index.html', context=context)


def about(request):
    return render(request, 'women/about.html', {'title': 'About'})


def addpage(request):
    return HttpResponse('<h1>Add page</h1>')


def show_post(request, post_id):
    return HttpResponse('<h1>Show post</h1>')


def contact(request):
    return HttpResponse('<h1>Contact</h1>')


def login(request):
    return HttpResponse('<h1>Login</h1>')


def categories(request, cat):
    if(request.POST):
        print(request.POST)

    return HttpResponse(f'<h1>Page of categories<h1><p>{cat}</p>')


def archive(request, year):
    if int(year) > 2020:
        return redirect('home', permanent=True)
        # raise Http404()

    return HttpResponse(f'<h1>Archive</h1><p>{year}</p>')


def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Page not found!</h1>')