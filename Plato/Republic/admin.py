from django.contrib import admin
from .models import Movie, Showtime, Ticket, Seat, Hall, Customer

admin.site.register(Movie)
admin.site.register(Showtime)
admin.site.register(Ticket)
admin.site.register(Hall)
admin.site.register(Customer)
admin.site.register(Seat)

