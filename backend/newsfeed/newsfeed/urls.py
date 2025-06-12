
"""URL configuration for the project."""

from django.urls import path, include  # utilities for routing URLs

# Map URL paths to views
urlpatterns = [
    path('api/', include('newsfeed.feed.urls')),  # include feed app routes under /api/
]
