from dockers.celery import app as celery

@celery.task()
def plus_task(value):
    return value
