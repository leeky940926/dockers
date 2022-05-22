CUSTOMIEZED_APPS = [
    'movies'
]

THIRD_PARTY_APPS = [
    'django_extensions',
    'corsheaders',
    'rest_framework',
    'rest_framework_swagger'
]

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
] + CUSTOMIEZED_APPS + THIRD_PARTY_APPS
