CELERY_BROKER_URL = "redis://localhost:6379/0"
CELERY_RESULT_BACKEND = "django-db"
CELERY_ACCEPT_CONTENT = [
    "json",
]
CELERY_TASK_SERIALIZER = "json"
CELERY_ENABLE_UTC = True
CELERY_TIMEZONE = "Asia/Seoul"
CELERY_BEAT_SCHEDULER = "django_celery_beat.schedulers:DatabaseScheduler"
CELERY_TASK_DEFAULT_QUEUE = "normal"
CELERY_TASK_DEFAULT_EXCHANGE = "normal"
CELERY_TASK_DEFAULT_ROUTING_KEY = "normal"
CELERY_TASK_QUEUES = {
    "low": {
        "exchange": "low",
        "routing_key": "low",
    },
    "normal": {
        "exchange": "normal",
        "routing_key": "normal",
    },
    "high": {
        "exchange": "high",
        "routing_key": "high",
    },
}
