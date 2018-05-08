from django.shortcuts import render
from django.http  import HttpResponse

# Create your views here.

def media_all(request):
    return render(request, 'all/all-media.html')
