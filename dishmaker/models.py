from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


class Ingredient(models.Model):
    name = models.CharField(max_length=30, unique=True)
    description = models.TextField(blank=True)
    # person_id = models.ForeignKey(Person, on_delete=models.CASCADE, related_name='Membership')
    # group_id = models.ForeignKey(Group, on_delete=models.CASCADE)
    # date_joined = models.DateField(auto_now=True)
    # invite_reason = models.CharField(max_length=100)

    def __str__(self):
        output = str(self.name)
        return output


class Dish(models.Model):
    name = models.CharField(max_length=30, unique=True)
    description = models.TextField(null=True)
    ingredients = models.ManyToManyField(Ingredient, through='IngredientQuantityInDishProxy')  # Won't be shown

    def __str__(self):
        output = str(self.name) + '\n' + str(self.description)
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
    created_on = models.DateTimeField(auto_now=True)
    description = models.TextField(null=True)
    ingredients = models.ManyToManyField(Ingredient, through='IngredientQuantityInDishProxy')  # Won't be shown

    def __str__(self):
        output = str(self.name) + '\n' + str(self.description)
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
    # dishrecipe_quantity = models.IntegerField(default=0,
    #                                           validators=[
    #                                             MinValueValidator(0),
    #                                           ])

    def __str__(self):
        output = '\n' + str(self.ingredient_id) + \
                 ' ' + str(self.dishrecipe_id) + \
                 '\nqn:' + str(self.ingredient_quantity)
        return output
