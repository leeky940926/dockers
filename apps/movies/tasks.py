from dockers.celery import app as celery

@celery.task(bind=True)
def plus_task():
    return 7