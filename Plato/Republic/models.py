from django.db import models

class Movie(models.Model):
    title = models.CharField(max_length=100)
    genres = models.ManyToManyField('Genre', related_name='movies', blank=True)
#     genre = models.CharField(max_length=15)
    release_year = models.IntegerField()
    duration_minutes = models.IntegerField(default=1, null=True, blank=True)
    age_rating = models.CharField(max_length=10)
    description = models.TextField()
    poster = models.ImageField(upload_to='posters/') 
    trailer = models.FileField(upload_to='trailers/', null=True, blank=True)

    def __str__(self):
        return self.title
    

    class Meta:
        verbose_name_plural = 'Movies'
        ordering = ['title']


class TVShow(models.Model):
    title = models.CharField(max_length=100)
    genres = models.ManyToManyField('Genre', related_name='tv_shows', blank=True)
#     genre = models.CharField(max_length=15)
    release_year = models.IntegerField()
    duration_minutes = models.IntegerField(default=1, null=True, blank=True)
    age_rating = models.CharField(max_length=10)
    description = models.TextField()
    poster = models.ImageField(upload_to='posters/') 
    trailer = models.FileField(upload_to='trailers/', null=True, blank=True)

    def __str__(self):
        return self.title
    

    class Meta:
        verbose_name_plural = 'Movies'
        ordering = ['title']


class Genre(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Genres"
        ordering = ['name']



class Customer(models.Model):
     name = models.CharField(max_length=30)
     surname = models.CharField(max_length=30)
     