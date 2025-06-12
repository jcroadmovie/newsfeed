
"""WSGI entry point for serving the Django application."""

import os  # access environment variables
from django.core.wsgi import get_wsgi_application  # returns WSGI callable

# Point Django at the settings module and create the WSGI application
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'newsfeed.settings')
application = get_wsgi_application()
