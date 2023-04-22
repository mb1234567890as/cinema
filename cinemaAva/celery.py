import os
from celery import Celery
from celery.schedules import crontab
8

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'cinemaAva.settings')

app = Celery('cinemaAva')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()
app.conf.beat_schedule = {
    'add-every-5 second': {
    'task': 'movie.tasks.create_random_user_accounts',
    'schedule': crontab(hour=11, minute=[53, 54, 55, 56], day_of_week=4),
    'args': (19, )
    }
}
app.conf.timezone = 'Asia/Bishkek'

# @app.on_after_configure.connect
# def setup_periodict_tasks(sender, **args):
