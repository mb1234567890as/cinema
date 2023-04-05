import django_filters.rest_framework
from django.shortcuts import render
from django.http import HttpResponse
from .models import *
from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveAPIView, DestroyAPIView, UpdateAPIView
from .serializers import *
from rest_framework import filters


class MovieFilter(django_filters.FilterSet):
    start_year = django_filters.NumberFilter(field_name='start_date__year')
    # start_date = django_filters.DateFromToRangeFilter()
    class Meta:
        model = Movie
        fields = ('start_year', )

class MovieListAPIView(ListAPIView):
    serializer_class = MovieSerializers
    filter_backends = [filters.SearchFilter, filters.OrderingFilter, django_filters.rest_framework.DjangoFilterBackend]
    filterset_fields = ('start_date',)
    search_fields = ('name', 'company')
    filterset_class = MovieFilter

    def get_queryset(self):
        queryset = Movie.objects.all()
        return queryset
    
class MovieCreateAPIView(CreateAPIView):
    serializer_class = MovieSerializers

    def get_queryset(self):
        queryset = Movie.objects.all()
        return queryset

class MovieRettrieveAPIView(RetrieveAPIView):
    serializer_class = MovieDetailSerializer
    queryset = Movie.objects.all()

class MovieDestroyAPIView(DestroyAPIView):
    serializer_class = MovieDetailSerializer
    queryset = Movie.objects.all()

class MovieUpdateAPIView(UpdateAPIView):
    serializer_class = MovieSerializers
    queryset = Movie.objects.all()

    # def put(self):
    #     queryset = Movie.objects.update()
    #     return queryset
    
    # def patch(self):
    #     queryset = Movie.objects.partial_update()
    #     return queryset

class JobListAPIVeiw(ListAPIView):
    serializer_class = JobSerializers
    filter_backends = [filters.SearchFilter, filters.OrderingFilter, django_filters.rest_framework.DjangoFilterBackend]
    # filterset_fields = ('name',)

    def get_queryset(self):
        return Job.objects.all()


class EmployeeList(ListAPIView):
    serializer_class = EmployeeSerializers
    filter_backends = [filters.SearchFilter, filters.OrderingFilter, django_filters.rest_framework.DjangoFilterBackend]
    filterset_fields = ('position__name',)
    
    def get_queryset(self):
        return Employee.objects.all()

class EmployeeCreateApiView(CreateAPIView):
    serializer_class = EmployeeSerializers
    queryset = Employee.objects.all()


class RoomList(ListAPIView):
    serializer_class = RoomSerializers
    filter_backends = [filters.SearchFilter, filters.OrderingFilter, django_filters.rest_framework.DjangoFilterBackend]
    filterset_fields = ('name',)
    search_fields = ('name', 'description',)

    def get_queryset(self):
        return Room.objects.all()

class RoomCreateAPIView(CreateAPIView):
    serializer_class = RoomSerializers

    def get_queryset(self):
        queryset = Room.objects.all()
        return queryset




class SeatList(ListAPIView):
    serializer_class = SeatSerializers
    filter_backends = [filters.SearchFilter, filters.OrderingFilter, django_filters.rest_framework.DjangoFilterBackend]
    filterset_fields = ('number',)
    search_fields = ('number', 'row',)

    def get_queryset(self):
        return Seat.objects.all()

class SeatCreate(CreateAPIView):
    serializer_class = SeatSerializers
    queryset = Seat.objects.all()

class SectorList(ListAPIView):
    serializer_class = SectorSerializers
    filter_backends = [filters.SearchFilter, filters.OrderingFilter, django_filters.rest_framework.DjangoFilterBackend]
    filterset_fields = ('name',)
    search_fields = ('name', 'description')


    def get_queryset(self):
        return Sector.objects.all()

class SectorCreateAPIView(CreateAPIView):
    serializer_class = SectorSerializers

    def get_queryset(self):
        queryset = Sector.objects.all()
        return queryset

# _____________________________________________
class SessionFilter(django_filters.FilterSet):
    start_date = django_filters.DateTimeFilter(field_name='start_date', lookup_expr='date')
    # start_date = django_filters.DateFromToRangeFilter()
    class Meta:
        model = Session
        fields = ('start_date', )

class SessionListAPIView(ListAPIView):
    serializer_class = SessionSerializers
    filter_backends = {filters.SearchFilter, filters.OrderingFilter, django_filters.rest_framework.DjangoFilterBackend}
    search_fields = ('movie__name',)
    # search_fields = ('movie', 'room', 'start_date', )
    filterset_class = SessionFilter


    def get_queryset(self):
        return Session.objects.all()

class SessionCreateAPIView(CreateAPIView):
    serializer_class = SessionSerializers

    def get_queryset(self):
        queryset = Session.objects.all()
        return queryset

class SessionRettrieveAPIView(RetrieveAPIView):
    serializer_class = SessionDetailSerializer
    queryset = Session.objects.all()






# +++++++++++++++++++++++++++++++++++++++++

class TicketPriceList(ListAPIView):
    serializer_class = TicketPriceSerializers
    filter_backends = [filters.SearchFilter, filters.OrderingFilter, django_filters.rest_framework.DjangoFilterBackend]
    filterset_fields = ('name',)

    def get_queryset(self):
        return TicketPrice.objects.all()
    
class TicketPriceCreateAPIView(CreateAPIView):
    serializer_class = TicketPriceSerializers

    def get_queryset(self):
        queryset = TicketPrice.objects.all()
        return queryset


class TicketList(ListAPIView):
    serializer_class = TicketSerializers
    filter_backends = [filters.SearchFilter, filters.OrderingFilter, django_filters.rest_framework.DjangoFilterBackend]
    filterset_fields = ('price__name',)

    def get_queryset(self):
        return Ticket.objects.all()

class TicketCreateAPIView(CreateAPIView):
    serializer_class = TicketSerializers

    def get_queryset(self):
        queryset = Ticket.objects.all()
        return queryset

class TicketRettrieveAPIView(RetrieveAPIView):
    serializer_class = TicketDetailSerializer
    queryset = Ticket.objects.all()

class TicketUpdateAPIView(UpdateAPIView):
    serializer_class = TicketDetailSerializer
    queryset = Ticket.objects.all()

class TicketDestroyAPIView(DestroyAPIView):
    serializer_class = TicketDetailSerializer
    queryset = Ticket.objects.all()






class MovingTicketList(ListAPIView):
    serializer_class = MovingTicketSerializers
    filter_backends = [filters.SearchFilter, filters.OrderingFilter, django_filters.rest_framework.DjangoFilterBackend]
    filterset_fields = ('ticket__price__name',)


    def get_queryset(self):
        return MovingTicket.objects.all()





























    # filterset_fields = ('name',)
# def index(request):
#     return HttpResponse('Привет! Мая первая ссылка!')


# def get_movies(request):
#     movies = Movie.objects.all()
#     result = ''
#     for movie in movies:
#         result += f'{movie.name}    {movie.long_time}мин     {movie.start_date} <br><br>'
#     return HttpResponse(result)

# def get_employee(request):
#     emploies = Employee.objects.all()
#     result = ''
#     for emploie in emploies:
#         result += f'{emploie.name}    {emploie.surname}    {emploie.patronymic}    {emploie.position.name}    {emploie.password} <br><br>'
#     return HttpResponse(result)

# def get_sector(request):
#     sectors = Sector.objects.all()
#     result = ''
#     for sector in sectors:
#         result += f'{sector.name} ----- Зал:{sector.room} -----  {sector.description} <br><br>'
#     return HttpResponse(result)

# def get_room(request):
#     rooms = Room.objects.all()
#     result = ''
#     for room in rooms:
#         result += f'{room.name} -----  {room.capacity} -----  {room.description} -----  Количество рядов:{row_count} -----  Количество мест:{seat_count} <br><br>'
#     return HttpResponse(result)


# def get_session(request):
#     sessions = Session.objects.all()
#     result = ''
#     for session in sessions:
#         result += f'фильм: {session.movie} зал: {session.room} дата начало: {session.start_date} <br><br>'
#     return HttpResponse(result)

# def get_job(request):
#     jobs = Job.objects.all()
#     result = ''
#     for job in jobs:
#         result += f'{job.name} <br><br>'
#     return HttpResponse(result)

# def get_seat(request):
#     seats = Seat.objects.all()
#     result = ''
#     for seat in seats:
#         result += f'ряд: {seat.row} -----  номер: {seat.number} зал: {seat.room} <br><br>'
#     return HttpResponse(result)

# def get_ticket(request):
#     tickets = Ticket.objects.all()
#     result = ''
#     for ticket in tickets:
#         result += f'сеанс: {ticket.session} -----  цена: {ticket.price} -----  места: {ticket.seat} -----  дата начало:{ticket.created_at} -----  статус: {ticket.status} <br><br>'
#     return HttpResponse(result)

# def get_movingticket(request):
#     movingtickets = MovingTicket.objects.all()
#     result = ''
#     for movingticket in movingtickets:
#         result += f'билеты: {movingticket.ticket} Дата начало:{movingticket.created_at} Сотрудники: {movingticket.employee} Операция: {movingticket.operation} <br><br>'
#     return HttpResponse(result)

# def get_ticketprice(request):
#     ticketprices = TicketPrice.objects.all()
#     result = ''
#     for ticketprice in ticketprices:
#         result += f'билет: {ticketprice.name} цена:{ticketprice.price} сеанс: {ticketprice.session} сектор: {ticketprice.sector} <br><br>'
#     return HttpResponse(result)