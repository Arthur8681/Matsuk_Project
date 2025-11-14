from django.shortcuts import render
from .models import *

# Create your views here.
def main(request):
    movie_autofill = Movie.objects.all()


    context = {
        'autofill': movie_autofill             
    }
    return render(request, 'Republic/Main.html', context)







def schindlers(request):
    return render(request, 'Republic/Schindlerslist.html')