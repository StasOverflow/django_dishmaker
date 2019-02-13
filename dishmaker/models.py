from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


# TODO: add a decorator, that replaces given classes __str__ method to its own. (to avoid code duplication)
# No clue how to make it

class Order(models.Model):
    name = models.CharField(max_length=30, unique=True)
    description = models.TextField(blank=True)
    # last_name = models.CharField(max_length=30)

    def __str__(self):
        output = str(self.name) + '\n' + str(self.description)
        return output


class Ingredient(models.Model):
    """
        I think this one is ment to be used for basic purposes, such as adding|deliting as is
        IMO this is possible, but requires additional amount of work
    """
    name = models.CharField(max_length=30, unique=True)
    description = models.TextField(blank=True)
    # person_id = models.ForeignKey(Person, on_delete=models.CASCADE, related_name='Membership')
    # group_id = models.ForeignKey(Group, on_delete=models.CASCADE)
    # date_joined = models.DateField(auto_now=True)
    # invite_reason = models.CharField(max_length=100)

    def __str__(self):
        output = str(self.name)
        return output


class DishRecipe(models.Model):
    name = models.CharField(max_length=30, unique=True)
    description = models.TextField(null=True)
    ingredients = models.ManyToManyField(Ingredient, through='IngredientQuantityInDishProxy')  # Won't be shown

    def __str__(self):
        output = str(self.name) + '\n' + str(self.description)
        return output


class IngredientQuantityInDishProxy(models.Model):
    ingredient_id = models.ForeignKey(Ingredient, on_delete=models.CASCADE,
                                      related_name='IngredientQuantityInDishProxy')
    dishrecipe_id = models.ForeignKey(DishRecipe, on_delete=models.CASCADE)
    ingredient_quantity = models.IntegerField(default=0,
                                              validators=[
                                                MinValueValidator(0),
                                              ])
    # dishrecipe_quantity = models.IntegerField(default=0,
    #                                           validators=[
    #                                             MinValueValidator(0),
    #                                           ])

    def __str__(self):
        output = '\n' + str(self.ingredient_id) + \
                 ' ' + str(self.dishrecipe_id) + \
                 '\nqn:' + str(self.ingredient_quantity)
        return output
# class MealIngredient(models.Model):
