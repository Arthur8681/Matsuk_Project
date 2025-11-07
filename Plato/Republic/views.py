from django.shortcuts import render
from .models import *

# Create your views here.
def main(request):
    Schindler = Movie.objects.get(title="Schindler's List")
    Shawshank = Movie.objects.get(title="The Shawshank Redemption")
    Star_Wars = Movie.objects.get(title="Star Wars: Episode V - The Empire Strikes Back")
    Interstellar = Movie.objects.get(title="Interstellar")
    Private_Ryan = Movie.objects.get(title="Saving Private Ryan")
    Whiplash = Movie.objects.get(title="Whiplash")
    Terrifier = Movie.objects.get(title="Terrifier")
    It = Movie.objects.get(title="It")
    Halloween = Movie.objects.get(title="Halloween")
    WW = Movie.objects.get(title="1917")
    Oil = Movie.objects.get(title="There Will Be Blood")
    Thing = Movie.objects.get(title="The Thing")


    context = {
        'Schindler': Schindler,
        'Shawshank': Shawshank,
        'Star_Wars': Star_Wars,
        'Interstellar': Interstellar,
        'Private_Ryan': Private_Ryan,
        'Whiplash': Whiplash,
        'Terrifier': Terrifier,
        'It': It,
        'Halloween': Halloween,
        'WW': WW,
        'Oil': Oil,
        'Thing': Thing           
    }
    return render(request, 'Republic/Main.html', context)