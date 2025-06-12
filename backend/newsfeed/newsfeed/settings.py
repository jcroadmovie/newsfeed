"""Django settings for the newsfeed project."""

import os  # operating system interfaces
from pathlib import Path  # convenient path object

# Base directory of the project
BASE_DIR = Path(__file__).resolve().parent.parent

# Security settings
SECRET_KEY = 'change-me'
DEBUG = True  # enable debug mode for development
ALLOWED_HOSTS = ['*']  # allow all hosts

# Applications enabled for this project
INSTALLED_APPS = [
    'corsheaders',                      # handle CORS headers
    'django.contrib.contenttypes',      # required Django contrib app
    'django.contrib.staticfiles',       # serve static files
    'rest_framework',                   # Django REST Framework
    'newsfeed.feed',                    # our feed application
]

# Minimal middleware stack
MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',  # injects CORS headers
    'django.middleware.common.CommonMiddleware',  # basic HTTP features
]

# Module containing URL declarations
ROOT_URLCONF = 'newsfeed.newsfeed.urls'

# Enable Django templates so the REST framework's browsable API works
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
            ],
        },
    },
]

# Entry point for WSGI servers
WSGI_APPLICATION = 'newsfeed.newsfeed.wsgi.application'

# Use a local SQLite database for simplicity
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# URL prefix for static files
STATIC_URL = '/static/'

# Disable Django authentication to keep the project minimal
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [],  # no auth classes
    'UNAUTHENTICATED_USER': None,          # skip auth user model
}

# Allow the local Next.js frontend to make cross-origin requests
CORS_ALLOWED_ORIGINS = [
    'http://localhost:3000',  # URL of the Next.js dev server
]
