CUSTOMIEZED_APPS = [
    'movies',
    'drf_yasg',
    'accounts'
]

THIRD_PARTY_APPS = [
    'django_extensions',
    'corsheaders',
    'rest_framework',
    'django_celery_results'
]

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
] + CUSTOMIEZED_APPS + THIRD_PARTY_APPS
