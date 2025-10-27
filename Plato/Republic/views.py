from django.shortcuts import render
from .models import *

# Create your views here.
def main(request):
    movie = Movie.objects.all()

    context = {
        'movies': movie,
    }
    return render(request, 'Republic/Main.html', context)