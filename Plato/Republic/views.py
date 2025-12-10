from django.shortcuts import render, get_object_or_404
from .models import *
from django.views.generic import DetailView
from django.views.generic import ListView
from django.db.models import Q

# Create your views here.
def main(request):
    movie_autofill = Movie.objects.all()


    context = {
        'autofill': movie_autofill             
    }
    return render(request, 'Republic/Main.html', context)


class MovieDetailView(DetailView):
    model = Movie
    template_name = 'Republic/movie_detail.html'  
    context_object_name = 'movie'  






class SearchResultsView(ListView):
    model = Movie
    template_name = 'Republic/search_results.html' 
    context_object_name = 'movies'  

    def get_queryset(self):
        query = self.request.GET.get('q')
        if query:
            queryset = Movie.objects.filter(
                Q(genres__name__icontains=query) | Q(title__icontains=query)
                ).distinct()

            return queryset
        return Movie.objects.none()  
    



def genres_list(request):
    genres = Genre.objects.all()
    return render(request, 'Republic/genres.html', {'genres': genres})

def genre_detail(request, genre_id):
    genre = get_object_or_404(Genre, pk=genre_id)
    movies = genre.movies.all()
    tv_shows = genre.tv_shows.all()  
    
    return render(request, 'Republic/genre_detail.html', {'genre': genre, 'movies': movies, 'tv_shows': tv_shows})