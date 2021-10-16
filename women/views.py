from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseNotFound, Http404

# Create your views here.

def index(request):
    return HttpResponse('Page of app women.')

def categories(request, cat):
    if(request.GET):
        print(request.GET)

    return HttpResponse(f'<h1>Page of categories<h1><p>{cat}</p>')

def archive(request, year):
    if int(year) > 2020:
        return redirect('home', permanent=True)
        # raise Http404()

    return HttpResponse(f'<h1>Archive</h1><p>{year}</p>')

def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Page not found!</h1>')