from django.db import models
from django.conf import settings
from apps.topics.models import Card

# Create your models here.
class FeedItem(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='feed_items')
    card = models.ForeignKey(Card, on_delete=models.CASCADE, related_name='feed_items')
    order = models.PositiveIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['order']
        unique_together = ['user', 'card']

    def __str__(self):
        return f'{self.user.email} - {self.card.title}'