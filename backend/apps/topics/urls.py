from django.urls import path
from .views import TopicCreateView, CategoryListView

urlpatterns = [
    path('create/', TopicCreateView.as_view(), name='topic-create'),
    path('categories/', CategoryListView.as_view(), name='category-list'),
]