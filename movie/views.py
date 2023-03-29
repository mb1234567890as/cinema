from django.shortcuts import render
from django.http import HttpResponse
from .models import *

def index(request):
    return HttpResponse('Привет! Мая первая ссылка!')


def get_movies(request):
    movies = Movie.objects.all()
    result = ''
    for movie in movies:
        result += f'{movie.name}    {movie.long_time}мин     {movie.start_date} <br><br>'
    return HttpResponse(result)

def get_employee(request):
    emploies = Employee.objects.all()
    result = ''
    for emploie in emploies:
        result += f'{emploie.name}    {emploie.surname}    {emploie.patronymic}    {emploie.position.name}    {emploie.password} <br><br>'
    return HttpResponse(result)

def get_sector(request):
    sectors = Sector.objects.all()
    result = ''
    for sector in sectors:
        result += f'{sector.name} ----- Зал:{sector.room} -----  {sector.description} <br><br>'
    return HttpResponse(result)

def get_room(request):
    rooms = Room.objects.all()
    result = ''
    for room in rooms:
        result += f'{room.name} -----  {room.capacity} -----  {room.description} -----  Количество рядов:{row_count} -----  Количество мест:{seat_count} <br><br>'
    return HttpResponse(result)


def get_session(request):
    sessions = Session.objects.all()
    result = ''
    for session in sessions:
        result += f'фильм: {session.movie} зал: {session.room} дата начало: {session.start_date} <br><br>'
    return HttpResponse(result)

def get_job(request):
    jobs = Job.objects.all()
    result = ''
    for job in jobs:
        result += f'{job.name} <br><br>'
    return HttpResponse(result)

def get_seat(request):
    seats = Seat.objects.all()
    result = ''
    for seat in seats:
        result += f'ряд: {seat.row} -----  номер: {seat.number} зал: {seat.room} <br><br>'
    return HttpResponse(result)

def get_ticket(request):
    tickets = Ticket.objects.all()
    result = ''
    for ticket in tickets:
        result += f'сеанс: {ticket.session} -----  цена: {ticket.price} -----  места: {ticket.seat} -----  дата начало:{ticket.created_at} -----  статус: {ticket.status} <br><br>'
    return HttpResponse(result)

def get_movingticket(request):
    movingtickets = MovingTicket.objects.all()
    result = ''
    for movingticket in movingtickets:
        result += f'билеты: {movingticket.ticket} Дата начало:{movingticket.created_at} Сотрудники: {movingticket.employee} Операция: {movingticket.operation} <br><br>'
    return HttpResponse(result)

def get_ticketprice(request):
    ticketprices = TicketPrice.objects.all()
    result = ''
    for ticketprice in ticketprices:
        result += f'билет: {ticketprice.name} цена:{ticketprice.price} сеанс: {ticketprice.session} сектор: {ticketprice.sector} <br><br>'
    return HttpResponse(result)