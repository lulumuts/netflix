from django.shortcuts import render
from django.http  import HttpResponse
from .models import Carousel,Movie
from . request import all_movies
# Create your views here.

def media_all(request):
    popular_movies = all_movies('popular')
    print(popular_movies)
    show = Carousel.show_all
    return render(request, 'all/all-media.html',{"show" : show,"popular_movies":popular_movies})

def media_search(request):
    return render(request, 'all/search.html')

def media_details(request):
    return render(request, 'all/details.html')

def media_rec(request):
    return render(request,'all/recc.html')
