# Generated by Django 4.1.7 on 2023-03-29 05:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Имя')),
                ('surname', models.CharField(max_length=100, verbose_name='Фамилия')),
                ('patronymic', models.CharField(max_length=100, verbose_name='Отчество')),
                ('password', models.CharField(max_length=100, verbose_name='Пароль')),
            ],
            options={
                'verbose_name': 'Сотрудник',
                'verbose_name_plural': 'Сотрудники',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Job',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Название')),
            ],
            options={
                'verbose_name': 'Должность',
                'verbose_name_plural': 'Должности',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Название')),
                ('long_time', models.IntegerField(help_text='В минутах', verbose_name='Длительность')),
                ('start_date', models.DateField(verbose_name='Дата выхода')),
                ('end_date', models.DateField(verbose_name='Дата окончания')),
                ('company', models.CharField(max_length=100, verbose_name='Прокатчик')),
            ],
            options={
                'verbose_name': 'Фильм',
                'verbose_name_plural': 'Фильмы',
                'ordering': ['start_date'],
            },
        ),
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Название')),
                ('capacity', models.IntegerField(verbose_name='Вместимость')),
                ('description', models.TextField(verbose_name='Описание')),
                ('row_count', models.IntegerField(verbose_name='Количество рядов')),
                ('seat_count', models.IntegerField(verbose_name='Количество мест')),
            ],
            options={
                'verbose_name': 'Зал',
                'verbose_name_plural': 'Залы',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Seat',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('row', models.IntegerField(verbose_name='Ряд')),
                ('number', models.IntegerField(verbose_name='Номер')),
                ('room', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='movie.room', verbose_name='Зал')),
            ],
            options={
                'verbose_name': 'Место',
                'verbose_name_plural': 'Места',
                'ordering': ['row', 'number'],
            },
        ),
        migrations.CreateModel(
            name='Sector',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Название')),
                ('description', models.TextField(verbose_name='Описание')),
                ('room', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='movie.room', verbose_name='Зал')),
            ],
            options={
                'verbose_name': 'Сектор',
                'verbose_name_plural': 'Секторы',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Session',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_date', models.DateTimeField(verbose_name='Дата начала')),
                ('movie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='movie.movie', verbose_name='Фильм')),
                ('room', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='movie.room', verbose_name='Зал')),
            ],
            options={
                'verbose_name': 'Сеанс',
                'verbose_name_plural': 'Сеансы',
                'ordering': ['start_date'],
            },
        ),
        migrations.CreateModel(
            name='TicketPrice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Название')),
                ('price', models.IntegerField(verbose_name='Цена')),
                ('sector', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='movie.sector', verbose_name='Сектор')),
                ('session', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='movie.session', verbose_name='Сеанс')),
            ],
            options={
                'verbose_name': 'Цена билета',
                'verbose_name_plural': 'Цены билетов',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Ticket',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
                ('status', models.CharField(choices=[('empty', 'Свободен'), ('reserved', 'Забронирован'), ('sold', 'Продан'), ('destroyed', 'Уничтожен')], default='empty', max_length=15, verbose_name='Статус')),
                ('price', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='movie.ticketprice', verbose_name='Цена')),
                ('seat', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='movie.seat', verbose_name='Место')),
                ('session', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='movie.session', verbose_name='Сеанс')),
            ],
            options={
                'verbose_name': 'Билет',
                'verbose_name_plural': 'Билеты',
                'ordering': ['session', 'price', 'seat'],
            },
        ),
        migrations.CreateModel(
            name='MovingTicket',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
                ('operation', models.CharField(max_length=100, verbose_name='Операция')),
                ('employee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='movie.employee', verbose_name='Сотрудник')),
                ('ticket', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='movie.ticket', verbose_name='Билет')),
            ],
            options={
                'verbose_name': 'Движение билета',
                'verbose_name_plural': 'Движения билетов',
                'ordering': ['ticket', 'created_at'],
            },
        ),
        migrations.AddField(
            model_name='employee',
            name='position',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='movie.job', verbose_name='Должность'),
        ),
    ]
