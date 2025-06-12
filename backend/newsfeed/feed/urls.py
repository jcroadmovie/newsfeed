
"""URL routes for the feed application."""

from django.urls import path  # URL helper
from .views import NewsFeedView, NewsFeedStreamView  # view classes

# Map endpoints to views
urlpatterns = [
    path('newsfeed/', NewsFeedView.as_view(), name='newsfeed'),  # list endpoint
    path('newsfeed/stream/', NewsFeedStreamView.as_view(), name='newsfeed-stream'),  # SSE stream
]
