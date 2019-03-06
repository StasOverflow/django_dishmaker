from django.test import TestCase
from .models import Dish, Ingredient, IngredientQuantityInDishProxy
from django.urls import reverse


# Create your tests here.
class DishTestCase(TestCase):

    test_dish_name = 'test_dish'
    other_name = 'other_dish'

    def setUp(self):
        self.dish = Dish.objects.create(name=self.test_dish_name, description='very interesting description')
        ingredient_1 = Ingredient.objects.create(name='cucumba', description='green brother')
        ingredient_2 = Ingredient.objects.create(name='coconut', description='shelly fella')

        ing_in_proxy_1 = IngredientQuantityInDishProxy.objects.create(ingredient_id=ingredient_1,
                                                                      ingredient_quantity=3,
                                                                      dishrecipe_id=self.dish)
        ing_in_proxy_2 = IngredientQuantityInDishProxy.objects.create(ingredient_id=ingredient_2,
                                                                      ingredient_quantity=11,
                                                                      dishrecipe_id=self.dish)

        # self.dish.ingredients.add(ingredient_1, ingredient_2)

    def test_dish_create(self):
        orders_count = Dish.objects.count()
        other_dish = Dish.objects.create(name=self.other_name)
        print(orders_count)
        self.client.post(reverse('dishmaker:order_add'), {'dish_id': other_dish.id})
        self.assertEquals(Dish.objects.count(), orders_count + 1)

    # def setUp(self):
    #     self.dish = Dish.objects.create(name="lollipop", description="Tasty lollipop")
    #     self.ingredient1 = Ingredient.objects.create(name="sugar")
    #     self.ingredient2 = Ingredient.objects.create(name="water")
    #     self.dish_ingredient1 = DishIngredient.objects.create(dish=self.dish, ingredient=self.ingredient1, quantity=100)
    #     self.dish_ingredient2 = DishIngredient.objects.create(dish=self.dish, ingredient=self.ingredient2, quantity=300)
    #     self.dish_invalid = Dish.objects.create(name="invalid dish", description="Anything invalid dish")

    def dish_create_via_crud(self):
        pass
