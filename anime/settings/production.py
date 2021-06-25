# Inherit from standard settings file for defaults
# Everything below will override our standard settings:
# Parse database configuration from $DATABASE_URL

import dj_database_url
import django_heroku

from .base import *

DEBUG = False
ALLOWED_HOSTS = ['herokuapp.com']

DATABASES['default'] = dj_database_url.config()
django_heroku.settings(locals())


MIDDLEWARE = [
    # Default Middleware ---------------------------------
    'django.middleware.security.SecurityMiddleware',
    # I added whitenoise here ----------------------
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
