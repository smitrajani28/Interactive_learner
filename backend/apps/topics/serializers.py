from rest_framework import serializers
from .models import Category, Card, Topic, Resource

class ResourceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Resource
        fields = ['id', 'title', 'url']

class CardSerializer(serializers.ModelSerializer):
    resources = ResourceSerializer(many=True, read_only=True)
    class Meta:
        model = Card
        fields = ['id', 'card_number', 'title', 'content', 'key_takeaway', 'resources']

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name']

class TopicSerializer(serializers.ModelSerializer):
    cards = CardSerializer(many=True, read_only=True)
    category = CategorySerializer(read_only=True)
    class Meta:
        model = Topic
        fields = ['id', 'name', 'description', 'blog_url', 'category', 'cards', 'created_at']
        read_only_fields = ['created_at']

class TopicCreateSerializer(serializers.ModelSerializer):
    category_name = serializers.CharField(write_only=True)
    class Meta:
        model = Topic
        fields = ['name', 'description', 'blog_url', 'category_name']