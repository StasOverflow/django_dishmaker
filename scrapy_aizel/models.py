from django.db import models


class Size(models.Model):
    size_title = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.size_title


class AizelClothItem(models.Model):
    title = models.CharField(max_length=100, unique=True)
    brand = models.CharField(max_length=100,)
    image = models.CharField(max_length=100,)
    price = models.IntegerField()
    size = models.ManyToManyField(Size, blank=True, null=True)
    descr = models.TextField()
    color = models.CharField(max_length=100,)

    def __str__(self):
        return self.title
