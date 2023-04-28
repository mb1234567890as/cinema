# Установка базового образа
FROM python:3.11.1


ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Установка рабочей директории
WORKDIR /app

#Установка зависимостей проекта в контейнер
COPY reg.txt .

RUN pip install --upgrade pip
# Установка зависимости проекта
RUN pip install -r reg.txt
# RUN pip install --no-cache-dir -r /app/req.txt

# Копировали файлов проекта в контейнер
COPY . .

# Запуск проекта
# CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]

# CMD ["celery", "-A", "cinemaAva", "worker"]

# CMD ["celery","-A","cinemaAva","beat","-l","info","--scheduler","django_celery_beat.schedulers:DatabaseScheduler"]

# CMD ["celery", "-A", "cinemaAva", "flower", "--adress=127.0.0.1", "--port=5566&"]