from django.db import models


class Size(models.Model):
    size_title = models.CharField(max_length=100, unique=True)


class AizelClothItem(models.Model):
    title = models.CharField(max_length=100, unique=True)
    brand = models.CharField(max_length=100,)
    image = models.CharField(max_length=100,)
    price = models.IntegerField()
    size = models.ForeignKey(Size, null=True, blank=True,  on_delete=models.CASCADE)
    descr = models.TextField()
    color = models.CharField(max_length=100,)
