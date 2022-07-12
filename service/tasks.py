from service.services import update_end_date
from djangoProject.celery import app
from celery import shared_task


@shared_task()
def update_db_every_minute():
    update_end_date()
