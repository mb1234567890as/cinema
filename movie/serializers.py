from rest_framework import serializers
from .models import *


class MovieSerializers(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ('id','name', 'long_time', 'start_date', 'end_date', 'company',  )
    
class MovieSessionSerializer(serializers.ModelSerializer):
    room = serializers.StringRelatedField()
    class Meta:
        model = Session
        fields = ('id','room', 'start_date', )

class MovieDetailSerializer(serializers.ModelSerializer):
    movie_session = MovieSessionSerializer(many=True, read_only=True)
    class Meta:
        model = Movie
        fields = ('id','name', 'long_time', 'start_date', 'end_date', 'company', 'movie_session', )


class JobSerializers(serializers.ModelSerializer):
    class Meta:
        model = Job
        fields = ('name',)


class EmployeeSerializers(serializers.ModelSerializer):
    position = serializers.CharField(source = 'position.name')
    class Meta:
        model = Employee
        fields = ('id','name', 'surname', 'patronymic','position', 'password', )

    def create(self, validated_data):
        position_name = validated_data.pop('position').get('name')
        job = Job.objects.get(name=position_name)
        employee = Employee.objects.create(position=job, **validated_data)
        return employee


class RoomSerializers(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = ('name', 'capacity', 'description', 'row_count', 'seat_count', )
        

class SeatSerializers(serializers.ModelSerializer):
    # room = serializers.CharField(source = 'room.name')
    class Meta:
        model = Seat
        fields = ('id', 'row', 'number', 'room',)


class SectorSerializers(serializers.ModelSerializer):
    # room = serializers.StringRelatedField()
    class Meta:
        model = Sector
        fields = ('id', 'name', 'room', 'description', )

class SectorDetailSerializer(serializers.ModelSerializer):
    movie_session = SectorSerializers(many=True, read_only=True)
    class Meta:
        model = Room
        fields = ('id', 'name', 'room', 'description', 'movie_session')

class SectorDetailSerializer(serializers.ModelSerializer):
    sector = SectorSerializers(many=True, read_only=True)
    class Meta:
        model = Sector
        fields = ('id', 'name', 'room', 'description', 'sector', )

class SessionSerializers(serializers.ModelSerializer):
    # movie = serializers.CharField(source = 'movie.name')
    # room = serializers.CharField(source = 'room.name')
    class Meta:
        model = Session
        fields = ('id', 'movie', 'room', 'start_date', )
    
    # def create(self, validated_data):
    #     movie_name = validated_data.pop('movie').get('name')
    #     movie = Movie.objects.get(name=movie_name)
    #     room_name = validated_data.pop('room').get('name')
    #     room = Room.objects.get(name=room_name)
    #     session = Session.objects.create(movie=movie, room=room, start_date=validated_data['start_date'])
    #     return session

        

class SessionDetailSerializer(serializers.ModelSerializer):
    session = SessionSerializers(many=True, read_only=True)
    class Meta:
        model = Session
        fields = ('id', 'movie', 'room', 'start_date',  'session' )



# ___________________________

class TicketPriceSerializers(serializers.ModelSerializer):
    # session = serializers.StringRelatedField()
    # sector = serializers.StringRelatedField()
    class Meta:
        model = TicketPrice
        fields = ('id', 'name', 'price', 'session', 'sector', )


class TicketSerializers(serializers.ModelSerializer):
    # price = serializers.CharField(source = 'price.name')
    class Meta:
        model = Ticket
        fields = ('id', 'session', 'price', 'seat', 'created_at', 'status', )

class TicketDetailSerializer(serializers.ModelSerializer):
    ticket = TicketSerializers(many=True, read_only=True)
    class Meta:
        model = Ticket
        fields = ('id', 'session', 'price', 'seat', 'created_at', 'status', 'ticket')

class MovingTicketSerializers(serializers.ModelSerializer):
    # ticket = serializers.CharField(source = 'ticket.price.name')
    class Meta:
        model = MovingTicket
        fields = ('id', 'ticket', 'created_at', 'operation', )
