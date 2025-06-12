import feedparser
from rest_framework.response import Response
from rest_framework.views import APIView

FEED_URL = 'https://feeds.feedburner.com/ft/PEfeed'

class NewsFeedView(APIView):
    def get(self, request):
        feed = feedparser.parse(FEED_URL)
        items = [
            {
                'title': entry.get('title'),
                'link': entry.get('link'),
                'published': entry.get('published'),
                'summary': entry.get('summary'),
            }
            for entry in feed.entries[:10]
        ]
        return Response(items)
