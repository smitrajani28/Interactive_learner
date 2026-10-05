from django.contrib import admin
from .models import Category, Topic, Card, Resource

# Register your models here.
admin.site.register(Category)
admin.site.register(Topic)
admin.site.register(Card)
admin.site.register(Resource)