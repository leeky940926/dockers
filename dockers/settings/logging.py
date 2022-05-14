LOGGING = {
    'disable_existing_loggers': False,
    'version': 1,
    'formatters': {
         'verbose': {
            'format': '{asctime} {levelname} {message}',
            'style': '{'
        },
    },
    'handlers': {
        'console': {
            'class'     : 'logging.StreamHandler',
            'formatter' : 'verbose',
            'level'     : 'DEBUG',
        }
    },
    'loggers': {
        'django.db.backends': {
            'handlers' : ['console'],
            'level'    : 'DEBUG',
            'propagate': False,
        },
    },
}