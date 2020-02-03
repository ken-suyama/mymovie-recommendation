from django.shortcuts import render, redirect
from django.http import Http404
from django.template.response import TemplateResponse
from django.db.models import Q
from django.views.generic import ListView
import csv
from .models import Movies, Tag
from .forms import MoviesForm
import pdb


def index(request):
    movies = Movies.objects.all()
    movies_list = Movies.objects.order_by('rank')[0:18]
    movies_list2 = Movies.objects.order_by('score').reverse()[0:18]
    recommends = Movies.objects.filter(check=False)
    random_list = recommends.order_by('?')[:1]
    recommend = random_list.get()
    query = request.GET.get('q')
    if query:
        movies = movies.filter(title__icontains=query)
    return TemplateResponse(request, 'index.html', {'movies':movies, 'movies_list':movies_list, 'movies_list2':movies_list2, 'query': query, 'recommend':recommend})

def all(request):

    movies_list = Movies.objects.order_by('rank')
    query = request.GET.get('q')
    if query:
        movies_list = movies_list.filter(title__icontains=query)
    return TemplateResponse(request, 'all.html', {'movies_list':movies_list, 'query': query})

def myrank(request):

    movies_list = Movies.objects.order_by('score').reverse()
    query = request.GET.get('q')
    if query:
        movies_list = movies_list.filter(title__icontains=query)
    return TemplateResponse(request, 'myrank.html', {'movies_list':movies_list, 'query': query})

def show(request, movie_id):
    
    movie = Movies.objects.get(id=movie_id)
    tags = movie.tags.all()
    if request.method == "POST":
        form = MoviesForm(request.POST, instance=movie)
        if form.is_valid():
            form.save()
            return TemplateResponse(request, 'show.html',{'form':form, 'movie':movie, 'tags':tags})
    else:
        form = MoviesForm(instance=movie)
    return TemplateResponse(request, 'show.html',{'form':form, 'movie':movie, 'tags':tags})




