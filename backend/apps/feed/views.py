from rest_framework.views import APIView
from rest_framework.response import Response
from .models import FeedItem
from .serializers import FeedItemSerializer


class FeedView(APIView):
    def get(self, request):
        feed_items = FeedItem.objects.filter(user=request.user).select_related('card__topic')
        return Response(FeedItemSerializer(feed_items, many=True).data)

