from django.shortcuts import render
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
                Q(title__icontains=query) | Q(genre__icontains=query)
            )

            return queryset
        return Movie.objects.none()  