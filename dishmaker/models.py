from django.db import models


# Create your models here.
class Order(models.Model):
    name = models.CharField(max_length=30)
    # last_name = models.CharField(max_length=30)


class Dish(models.Model):
    name = models.CharField(max_length=30)
    # members = models.ManyToManyField(Person, through='Membership')  # Won't be shown


class Ingredient(models.Model):
    name = models.CharField(max_length=30)
    # person_id = models.ForeignKey(Person, on_delete=models.CASCADE, related_name='Membership')
    # group_id = models.ForeignKey(Group, on_delete=models.CASCADE)
    # date_joined = models.DateField(auto_now=True)
    # invite_reason = models.CharField(max_length=100)
