from django.db import models


# Create your models here.
class Order(models.Model):
    name = models.CharField(max_length=30)
    description = models.TextField(default="")
    # last_name = models.CharField(max_length=30)

    def __str__(self):
        output = str(self.name) + str(self.description)
        return output


class DishRecipe(models.Model):
    name = models.CharField(max_length=30)
    description = models.TextField(default="unset")
    # members = models.ManyToManyField(Person, through='Membership')  # Won't be shown

    def __str__(self):
        output = str(self.name) + str(self.description)
        return output


class Ingredient(models.Model):
    name = models.CharField(max_length=30)
    description = models.TextField(default="unset")
    # person_id = models.ForeignKey(Person, on_delete=models.CASCADE, related_name='Membership')
    # group_id = models.ForeignKey(Group, on_delete=models.CASCADE)
    # date_joined = models.DateField(auto_now=True)
    # invite_reason = models.CharField(max_length=100)

    def __str__(self):
        output = str(self.name) + str(self.description)
        return output
