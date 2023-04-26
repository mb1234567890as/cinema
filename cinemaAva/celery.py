import os
from celery import Celery
from celery.schedules import crontab


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'cinemaAva.settings')

app = Celery('cinemaAva')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()
# app.conf.beat_schedule = {
#     'add-every-5 second': {
#     'task': 'movie.tasks.send_to_users',
#     'schedule': crontab(minute='*/1'),
#     # 'args': (19, )
#     }
# }
# app.conf.timezone = 'Asia/Bishkek'
















# app = Celery('cinemaAva')
# app.config_from_object('django.conf:settings', namespace='CELERY')
# app.autodiscover_tasks()
# app.conf.beat_schedule = {
#     'add-every-1 day': {
#     'task': 'movie.tasks.send_mail_task',
#     'schedule': crontab(hour=0,minute=[1],day_of_week=5),
#     'args':(19, )
#     }
# }






# @app.on_after_configure.connect
# def setup_periodict_tasks(sender, **args):