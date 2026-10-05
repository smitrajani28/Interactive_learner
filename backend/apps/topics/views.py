from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Category, Topic
from .serializers import CategorySerializer, TopicSerializer, TopicCreateSerializer


class TopicCreateView(APIView):
    def post(self, request):
        serializer = TopicCreateSerializer(data = request.data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
        category_name = serializer.validated_data.pop('category_name')
        category, _ = Category.objects.get_or_create(name=category_name)

        topic = Topic.objects.create(
            user = request.user,
            category = category,
            **serializer.validated_data
        )

        return Response(TopicSerializer(topic).data, status=status.HTTP_201_CREATED)

class CategoryListView(APIView):
    def get(self, request):
        categories = Category.objects.filter(topics__user=request.user).distinct()
        return Response(CategorySerializer(categories, many=True).data)