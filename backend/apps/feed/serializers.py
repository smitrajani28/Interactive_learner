from rest_framework import serializers
from .models import FeedItem
from apps.topics.serializers import CardSerializer

class FeedItemSerializer(serializers.ModelSerializer):
    card = CardSerializer(read_only=True)
    class Meta:
        model = FeedItem
        fields = ['id', 'card', 'order']