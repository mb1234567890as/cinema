from django.contrib import admin
from .models import *

@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'long_time', 'start_date', 'end_date', 'company', )
    list_filter = ('start_date',)
    search_fields = ('id', 'name', 'company',)
    list_display_links = ('id', 'name',)




# admin.site.register(Movie, MovieAdmin)
admin.site.register(Room)
admin.site.register(Job)
admin.site.register(Employee)
admin.site.register(Ticket)
admin.site.register(Session)
admin.site.register(Seat)
admin.site.register(Sector)
admin.site.register(TicketPrice)
admin.site.register(MovingTicket)
