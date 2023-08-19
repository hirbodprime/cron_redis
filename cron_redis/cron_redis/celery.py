# celery.py

from __future__ import absolute_import, unicode_literals
import os
from celery import Celery
from cron_app.tasks import my_celery_task

# Set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'cron_redis.settings')

app = Celery('cron_redis')

# Load task modules from all registered Django app configs.
app.config_from_object('django.conf:settings', namespace='CELERY')

# Auto-discover tasks in all apps
app.autodiscover_tasks()

@app.task(bind=True)
def debug_task(self):
    print('Request: {0!r}'.format(self.request))

# Schedule the task to run every second
app.conf.beat_schedule = {
    'my-task-every-second': {
        'task': 'cron_app.tasks.my_celery_task',
        'schedule': 10,  # Every second
    },
}
