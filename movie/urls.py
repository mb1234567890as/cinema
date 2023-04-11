from django.contrib import admin
from django.urls import path
from . import views 
# from rest_framework.authtoken import views as auth_views


urlpatterns = [
    path('api-token-auth/', views.AuthTokenView.as_view(), name='api_auth'),
    path('api-token-authout/', views.AuthTokenViewOut.as_view(), name='api_auth'),

    path('movie/', views.MovieListAPIView.as_view()),
    path('movie/create/', views.MovieCreateAPIView.as_view()),
    path('movie/<int:pk>/', views.MovieRettrieveAPIView.as_view(), name='movie_retrieve'),
    path('movie/delete/<int:pk>/', views.MovieDestroyAPIView.as_view(), name='movie_delete'),
    path('movie/update<int:pk>/', views.MovieUpdateAPIView.as_view(), name='movie_update'),

    path('job/', views.JobListAPIVeiw.as_view()),

    path('employee/', views.EmployeeList.as_view()),
    path('employee/create/', views.EmployeeCreateApiView.as_view()),

    path('room/', views.RoomList.as_view()),
    path('room/create/', views.RoomCreateAPIView.as_view()),

    path('seat/', views.SeatList.as_view()),
    path('seat/create/', views.SeatCreate.as_view()),

    path('sector/', views.SectorList.as_view()),
    path('sector/create/', views.SectorCreateAPIView.as_view()),
    path('sector/rud/<int:pk>/', views.SectorRUDAPIView.as_view(), name='sector_RUD_retrieve'),
    
    path('ticketprice/', views.TicketPriceList.as_view()),
    path('ticketprice/create/', views.TicketPriceCreateAPIView.as_view()),

    path('ticket/', views.TicketList.as_view()), 
    path('ticket/create/', views.TicketCreateAPIView.as_view()),
    path('ticket/<int:pk>/', views.TicketRettrieveAPIView.as_view(), name='ticket_retrieve'),
    path('ticket/delete/<int:pk>/', views.TicketDestroyAPIView.as_view(), name='ticket_delete'),
    path('ticket/update<int:pk>/', views.TicketUpdateAPIView.as_view(), name='ticket_update'),

    path('movingticket/', views.MovingTicketList.as_view()),
    path('movingticket/create/', views.MovingTicketCreateAPIViews.as_view()),
    path('movingticket/<int:pk>/', views.MovingTicketRetrieveAPIView.as_view()),
    

    path('session/', views.SessionListAPIView.as_view()),
    path('session/create/', views.SessionCreateAPIView.as_view()),
    path('session/<int:pk>/', views.SessionRettrieveAPIView.as_view(), name='session_retrieve'),

]














    # path('firsturl/', view=views.index, name='index'),
    # path('movies/', view=views.get_movies, name='movies'),
    # path('emploies/', view=views.get_employee, name='emploies'),
    # path('sector/', view=views.get_sector, name='sector'),
    # path('room/', view=views.get_room, name='room'),
    # path('session/', view=views.get_session, name='session'),
    # path('job/', view=views.get_job, name='job'),
    # path('seat/', view=views.get_seat, name='seat'),
    # path('ticket/', view=views.get_ticket, name='ticket'),
    # path('movingticket/', view=views.get_movingticket, name='movingticket'),
    # path('ticketprice/', view=views.get_ticketprice, name='ticketprice'),
# ]