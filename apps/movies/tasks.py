from dockers.celery import app as celery
from django.utils import timezone

@celery.task(bind=True)
def plus_task(self):
    print("UTC : ", timezone.now())
    print("SEOUL : ", timezone.now().astimezone())
    return 7