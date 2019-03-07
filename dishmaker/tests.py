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

    def test_dish__via_crud(self):
        orders_count = Dish.objects.count()
        print('order count:', orders_count)
        ingredient_1 = Ingredient.objects.create(name='sample_ingredient_1', description='sample description 1')
        ingredient_2 = Ingredient.objects.create(name='sample_ingredient_2', description='sample description 2')

        quasi_post_data = {
            'csrfmiddlewaretoken': ['00yxTw40sqf21KF4jnAsqnecnu5vJZdOCZ0gC9aQlCnPNEfFcMpSJQirxXiYlT2s'],
            'name': 'posted_dish',
            'description': ['El dishio with engridientos'],
            'dishrecipe-TOTAL_FORMS': ['2'],
            'dishrecipe-INITIAL_FORMS': ['0'],
            'dishrecipe-MIN_NUM_FORMS': ['0'],
            'dishrecipe-MAX_NUM_FORMS': ['1000'],
            'dishrecipe-0-ingredient_id': ['2'],
            'dishrecipe-0-ingredient_quantity': ['3'],
            'dishrecipe-0-id': [''],
            'dishrecipe-0-dishrecipe_id': [''],
            'dishrecipe-1-ingredient_id': ['5'],
            'dishrecipe-1-ingredient_quantity': ['1'],
            'dishrecipe-1-id': [''],
            'dishrecipe-1-dishrecipe_id': ['']
        }

        self.client.post(reverse('dishmaker:dish_add'), quasi_post_data)
        self.assertEquals(Dish.objects.count(), orders_count + 1)
        print('order count after creation', Dish.objects.count())
