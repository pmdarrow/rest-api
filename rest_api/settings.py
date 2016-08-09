"""
Django settings for rest_api project.
"""
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Note: normally I would pull this in from an environment variable, but given
# this is just a demo project, I've opted to leave it here.
SECRET_KEY = 'aa!4_+x++p9i#ckc!c2e7@hbhztq3vc1=po&ga*futri#%qm4='

# Set to true for easy demoing. Should not be true in production.
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'users',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.middleware.common.CommonMiddleware',
]

ROOT_URLCONF = 'rest_api.urls'

WSGI_APPLICATION = 'rest_api.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.10/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

USE_TZ = True
