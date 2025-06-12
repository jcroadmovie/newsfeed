"""Views exposing RSS feed data via REST and SSE."""

import feedparser  # library to parse RSS/Atom feeds
from rest_framework.response import Response  # standard DRF response class
from rest_framework.views import APIView  # base API view class
from django.http import StreamingHttpResponse  # for server-sent events
import json  # to encode items as JSON strings

# RSS feed used as the data source
FEED_URL = 'https://www.nytimes.com/svc/collections/v1/publish/http://www.nytimes.com/topic/subject/private-equity/rss.xml'


def parse_feed():
    """Parse the RSS feed and return a list of items."""
    feed = feedparser.parse(FEED_URL)  # download and parse the XML
    return [
        {
            'title': entry.get('title'),       # headline text
            'link': entry.get('link'),         # URL of the article
            'published': entry.get('published'),  # publication datetime
            'summary': entry.get('summary'),   # short summary HTML
        }
        for entry in feed.entries[:10]  # limit to first 10 entries
    ]

class NewsFeedView(APIView):
    """Return the latest RSS items as JSON."""

    def get(self, request):
        return Response(parse_feed())  # send parsed feed as JSON list


class NewsFeedStreamView(APIView):
    """Stream RSS items as Server-Sent Events."""

    def get(self, request):
        items = parse_feed()  # fetch items once

        def event_stream():
            for item in items:  # iterate over each item
                yield f"data: {json.dumps(item)}\n\n"  # format as SSE message

        # Return a streaming response with proper content type
        return StreamingHttpResponse(event_stream(), content_type='text/event-stream')
