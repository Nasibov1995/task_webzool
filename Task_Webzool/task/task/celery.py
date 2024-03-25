import os

from celery import Celery

from celery.schedules import crontab

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'task.settings')

app = Celery('task')


app.config_from_object('django.conf:settings', namespace='CELERY')


app.conf.beat_schedule = {
    "cron": {
        
        "task": "app.tasks.reactivation",
        "schedule": crontab(hour="*")
        
        }
}

app.autodiscover_tasks()
