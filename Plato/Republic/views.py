from django.shortcuts import render
from .models import *
from django.views.generic import DetailView

# Create your views here.
def main(request):
    movie_autofill = Movie.objects.all()


    context = {
        'autofill': movie_autofill             
    }
    return render(request, 'Republic/Main.html', context)


class MovieDetailView(DetailView):
    model = Movie
    template_name = 'Republic/movie_detail.html'  # We'll create this template next
    context_object_name = 'movie'  # This makes {{ movie }} available in the template