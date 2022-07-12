from celery import Celery
from celery.schedules import crontab
import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'djangoProject.settings')
app = Celery('service')
app.config_from_object('django.conf:settings')

# Load task modules from all registered Django app configs.
app.autodiscover_tasks()

# app.conf.beat_schedule = {
#     'update-db-every-single-minute': {
#         'task': 'service.tasks.update_db_every_minute',
#         'schedule': crontab(),  # change to `crontab(minute=0, hour=0)` if you want it to run daily at midnight
#     },
# }
