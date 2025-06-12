import feedparser
from rest_framework.response import Response
from rest_framework.views import APIView
from django.http import StreamingHttpResponse
import json

# RSS feed used as the data source
FEED_URL = 'https://www.nytimes.com/svc/collections/v1/publish/http://www.nytimes.com/topic/subject/private-equity/rss.xml'


def parse_feed():
    """Parse the RSS feed and return a list of items."""
    feed = feedparser.parse(FEED_URL)
    return [
        {
            'title': entry.get('title'),
            'link': entry.get('link'),
            'published': entry.get('published'),
            'summary': entry.get('summary'),
        }
        for entry in feed.entries[:10]
    ]

class NewsFeedView(APIView):
    def get(self, request):
        return Response(parse_feed())


class NewsFeedStreamView(APIView):
    """Stream RSS items as Server-Sent Events."""

    def get(self, request):
        items = parse_feed()

        def event_stream():
            for item in items:
                yield f"data: {json.dumps(item)}\n\n"

        return StreamingHttpResponse(event_stream(), content_type='text/event-stream')
