from django.db import models


class Note(models.Model):
    title = models.CharField(max_length=30, unique=True, required=True)
    description = models.TextField(blank=False)
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
