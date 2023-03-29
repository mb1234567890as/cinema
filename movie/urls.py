from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('firsturl/', view=views.index, name='index'),
    path('movies/', view=views.get_movies, name='movies'),
    path('emploies/', view=views.get_employee, name='emploies'),
    path('sector/', view=views.get_sector, name='sector'),
    path('room/', view=views.get_room, name='room'),
    path('session/', view=views.get_session, name='session'),
    path('job/', view=views.get_job, name='job'),
    path('seat/', view=views.get_seat, name='seat'),
    path('ticket/', view=views.get_ticket, name='ticket'),
    path('movingticket/', view=views.get_movingticket, name='movingticket'),
    path('ticketprice/', view=views.get_ticketprice, name='ticketprice'),
]