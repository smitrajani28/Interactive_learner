from django.db import models
from django.conf import settings
# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.name

class Topic(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='topics')
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, related_name='topics')
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    blog_url = models.URLField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Card(models.Model):
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE, related_name='cards')
    card_number = models.PositiveIntegerField()
    title = models.CharField(max_length=255)
    content = models.TextField()
    key_takeaway = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['card_number']
    
    def __str__(self):
        return f'{self.topic.name} - Card {self.card_number}'

class Resource(models.Model):
    card = models.ForeignKey(Card, on_delete=models.CASCADE, related_name='resources')
    title = models.CharField(max_length=255)
    url = models.URLField()

    def __str__(self):
        return self.title

