from django.contrib import admin
from .models import Movie, Customer, TVShow, Genre

admin.site.register(Movie)
admin.site.register(TVShow)
admin.site.register(Genre)
admin.site.register(Customer)
