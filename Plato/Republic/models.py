from django.db import models

class Movie(models.Model):
    title = models.CharField(max_length=30)
    genre = models.CharField(max_length=15)
    duration = models.TimeField()
    age_rating = models.CharField(max_length=10)
    description = models.TextField()

    def __str__(self):
        return f"{self.title} {self.genre}"
    

    class Meta:
        verbose_name_plural = 'Movies'
        ordering = ['genre']

class Showtime(models.Model):
        movie = models.ForeignKey(Movie)
        hall = models.ForeignKey('Hall')
        start_time = models.DateTimeField()
        price = models.DecimalField()
        

        class Meta:
             ordering = ['start_time']


class Hall(models.Model):
     name = models.CharField(max_length=20)
     capacity = models.DecimalField()
     hall_type = models.BooleanField()




     class Meta:
          verbose_name_plural = 'Halls'
          ordering = ['hall_type']


class Seat(models.Model):
     hall = models.ForeignKey(Hall)
     row_number = models.DecimalField()
     seat_number = models.DecimalField()
     seat_type = models.BooleanField()


     class Meta:
          verbose_name_plural = 'Seats'
          ordering = ['row_number']


class Ticket(models.Model):
     showtime = models.ForeignKey(Showtime)
     seat = models.ForeignKey(Seat)
     customer = models.ForeignKey('Customer')
     purchase_date= models.DateTimeField()
     final_price = models.DecimalField()
     status = models.BooleanField()

     class Meta:
          verbose_name_plural = 'Tickets'
          ordering = ['status']


class Customer(models.Model):
     name = models.CharField(max_length=30)
     surname = models.CharField(max_length=30)
     