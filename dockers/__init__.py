from .celery import app as celery_app

#둘 중 뭘하든 상관없음

__all__ = ['celery_app']
#__all__ = ('celery_app',)