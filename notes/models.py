from django.db import models
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.fields import GenericRelation


class NotedItem(models.Model):
    note = models.CharField(max_length=30, unique=True, blank=False)
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField(blank=False)
    content_object = GenericForeignKey('content_type', 'object_id')
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.note
