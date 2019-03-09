from django.db import models
from django.core.validators import MinValueValidator
from django.contrib.contenttypes.fields import GenericRelation
from notes.models import NotedItem
from django.contrib.auth.models import User


class Ingredient(models.Model):
    name = models.CharField(max_length=30, unique=True)
    description = models.TextField(blank=True)
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        output = str(self.name)
        return output


class Dish(models.Model):
    name = models.CharField(max_length=30, unique=True)
    description = models.TextField(null=True, blank=True)
    ingredients = models.ManyToManyField(Ingredient, through='IngredientQuantityInDishProxy')  # Won't be shown
    created_on = models.DateTimeField(auto_now_add=True)
    notes = GenericRelation(NotedItem, related_query_name='dish')
    author = models.ForeignKey(User, null=True, blank=True,  on_delete=models.CASCADE)

    def __str__(self):
        output = str(self.name)
        return output


class Order(models.Model):
    dish_id = models.ForeignKey(
                            Dish,
                            related_name="dish",
                            on_delete=models.SET_NULL,
                            blank=True,
                            null=True,
                            default=None,
                        )
    created_on = models.DateTimeField(auto_now_add=True)
    description = models.TextField(null=True)
    ingredients = models.ManyToManyField(Ingredient, through='IngredientQuantityInDishProxy')  # Won't be shown
    notes = GenericRelation(NotedItem, related_query_name='order')
    author = models.ForeignKey(User, null=True, blank=True,  on_delete=models.CASCADE)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        output = 'Order: ' + str(self.id)
        return output


class IngredientQuantityInDishProxy(models.Model):
    ingredient_id = models.ForeignKey(
                            Ingredient,
                            related_name='ing_dish_quan',
                            on_delete=models.SET_NULL,
                            blank=True,
                            null=True,
                            default=None,
                        )
    dishrecipe_id = models.ForeignKey(
                            Dish,
                            related_name='dishrecipe',
                            on_delete=models.SET_NULL,
                            blank=True,
                            null=True,
                            default=None,
                        )
    order_id = models.ForeignKey(
                            Order,
                            related_name='order',
                            on_delete=models.SET_NULL,
                            blank=True,
                            null=True,
                            default=None,
                        )
    ingredient_quantity = models.IntegerField(
                            default=0,
                            validators=[
                                    MinValueValidator(1),
                                ],
                            null=False,
                        )

    def __str__(self):
        output = '\n' + str(self.ingredient_id) + \
                 ' ' + str(self.dishrecipe_id) + \
                 '\nqn:' + str(self.ingredient_quantity) + '\n'
        return output
