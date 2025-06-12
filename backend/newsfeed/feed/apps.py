
"""Django app configuration for the feed app."""

from django.apps import AppConfig  # base class for app configs

class FeedConfig(AppConfig):
    """Register the feed application with Django."""

    default_auto_field = 'django.db.models.BigAutoField'  # model primary key type
    name = 'newsfeed.feed'  # dotted path to the app package
