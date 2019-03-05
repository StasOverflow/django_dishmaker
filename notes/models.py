from django.db import models
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.fields import GenericRelation


class Note(models.Model):
    title = models.CharField(max_length=30, unique=True, blank=False)
    created_on = models.DateTimeField(auto_now_add=True)
    tags = GenericRelation('NotedItem')

    def __str__(self):
        return self.title


class NotedItem(models.Model):
    note = models.ForeignKey(Note, on_delete=models.CASCADE, related_name='noted_item')
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField(blank=False)
    content_object = GenericForeignKey('content_type', 'object_id')

    def __str__(self):
        return self.note
