import os
import django
from celery import Celery
from celery.schedules import crontab
from django.conf import settings

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'main.settings')
django.setup()
app = Celery('main') # название приложения
app.config_from_object('django.conf:settings')
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS) # для поисков задач

app.conf.beat_schedule = {
    'send_spam_from_john': {
        'task': '',
        'schedule': crontab(minute='*/1')
    }
}