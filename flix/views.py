from django.shortcuts import render
from django.http  import HttpResponse

# Create your views here.

def media_all(request):
    return render(request, 'all/all-media.html')

def media_search(request):
    return render(request, 'all/search.html')

def media_details(request):
    return render(request, 'all/details.html')

def media_rec(request):
    return render(request,'all/recc.html')
