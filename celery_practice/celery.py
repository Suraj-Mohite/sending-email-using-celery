
from __future__ import absolute_import,unicode_literals
import os
from celery import Celery
from django.conf import settings
from celery.schedules import crontab


# Set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'celery_practice.settings')

app = Celery('celery_practice')

app.conf.enable_utc=False
app.conf.update(timezone='Asia/Kolkata')

# Using a string here means the worker doesn't have to serialize
# the configuration object to child processes.
# - namespace='CELERY' means all celery-related configuration keys
#   should have a `CELERY_` prefix.
# app.config_from_object('django.conf:settings', namespace='CELERY')
app.config_from_object(settings, namespace='CELERY')


#celery beat
app.conf.beat_schedule={
    'send-mail-everyday':{
        'task':'send_mail.tasks.send_mail_func',
        'schedule': crontab(hour=12,minute=55)
    }
}
# Load task modules from all registered Django apps.
app.autodiscover_tasks()


@app.task(bind=True)
def debug_task(self):
    print(f'Request: {self.request!r}')