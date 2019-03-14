from __future__ import absolute_import, unicode_literals
import os
from celery import Celery
from celery.schedules import crontab
from dish_composer.settings import BROKER_URL
from dish_composer.settings import CELERY_RESULT_BACKEND


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'dish_composer.settings')

app = Celery('dishmaker',
             backend=CELERY_RESULT_BACKEND,
             broker=BROKER_URL)

app.config_from_object('django.conf:settings', namespace='CELERY')

app.conf.update({'beat_schedule': {
    'check_expiration_time': {
        'task': 'dishmaker.tasks.flag_expired_order',
        'schedule': crontab(minute='*/1'),  # minute='2, 35' << only 2nd and 35th minute of an hour
        'args': ('', )
        },
    }
})   # accepts a dict with configurations
app.conf.timezone = 'UTC'

app.autodiscover_tasks()


@app.task(bind=True)
def debug_task(self):
    print('Request: {0!r}'.format(self.request))
