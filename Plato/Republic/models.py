from django.db import models

class Movie(models.Model):
    title = models.CharField(max_length=100)
    genre = models.CharField(max_length=15)
    duration_minutes = models.IntegerField(default=1, null=True, blank=True)
    age_rating = models.CharField(max_length=10)
    description = models.TextField()

    def __str__(self):
        return f"{self.title} {self.genre}"
    

    class Meta:
        verbose_name_plural = 'Movies'
        ordering = ['genre']

class Showtime(models.Model):
        movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
        hall = models.ForeignKey('Hall', on_delete=models.CASCADE)
        start_time = models.DateTimeField()
        price = models.DecimalField(max_digits=8, decimal_places=2)
        

        class Meta:
             ordering = ['start_time']


class Hall(models.Model):
     name = models.CharField(max_length=20)
     capacity = models.IntegerField()
     is_hall_vip = models.BooleanField()




     class Meta:
          verbose_name_plural = 'Halls'
          ordering = ['is_hall_vip']


class Seat(models.Model):
     hall = models.ForeignKey(Hall, on_delete=models.CASCADE)
     row_number = models.IntegerField()
     seat_number = models.IntegerField()
     is_seat_vip = models.BooleanField()


     class Meta:
          verbose_name_plural = 'Seats'
          ordering = ['row_number']


class Ticket(models.Model):
     showtime = models.ForeignKey(Showtime, on_delete=models.CASCADE)
     seat = models.ForeignKey(Seat, on_delete=models.CASCADE)
     customer = models.ForeignKey('Customer', on_delete=models.CASCADE)
     purchase_date= models.DateTimeField()
     final_price = models.DecimalField(max_digits=8, decimal_places=2)
     is_paid = models.BooleanField()

     class Meta:
          verbose_name_plural = 'Tickets'
          ordering = ['is_paid']


class Customer(models.Model):
     name = models.CharField(max_length=30)
     surname = models.CharField(max_length=30)
     