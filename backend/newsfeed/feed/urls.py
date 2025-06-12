from django.urls import path
from .views import NewsFeedView, NewsFeedStreamView

urlpatterns = [
    path('newsfeed/', NewsFeedView.as_view(), name='newsfeed'),
    path('newsfeed/stream/', NewsFeedStreamView.as_view(), name='newsfeed-stream'),
]
