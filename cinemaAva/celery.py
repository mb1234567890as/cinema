import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'cinemaAva.settings')

app = Celery('cinemaAva')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()