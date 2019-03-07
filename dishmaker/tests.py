from django.test import TestCase
from .models import Dish, Ingredient, IngredientQuantityInDishProxy, Order
from django.urls import reverse


# Create your tests here.
class DishTestCase(TestCase):

    test_dish_name = 'test_dish'
    other_name = 'other_dish'

    def setUp(self):
        self.dish = Dish.objects.create(name=self.test_dish_name, description='very interesting description')
        self.wrong_dish = Dish.objects.create(name='fail_dish', description='i will fail')
        ingredient_1 = Ingredient.objects.create(name='cucumba', description='green brother')
        ingredient_2 = Ingredient.objects.create(name='coconut', description='shelly fella')

        ing_in_proxy_1 = IngredientQuantityInDishProxy.objects.create(ingredient_id=ingredient_1,
                                                                      ingredient_quantity=3,
                                                                      dishrecipe_id=self.dish)
        ing_in_proxy_2 = IngredientQuantityInDishProxy.objects.create(ingredient_id=ingredient_2,
                                                                      ingredient_quantity=11,
                                                                      dishrecipe_id=self.dish)

        ing_in_proxy_3 = IngredientQuantityInDishProxy.objects.create(ingredient_id=ingredient_2,
                                                                      ingredient_quantity=11,
                                                                      dishrecipe_id=self.wrong_dish)

    def test_dish_creation_via_crud(self):
        dish_count = Dish.objects.count()

        quasi_post_data = {
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
        }

        self.client.post(reverse('dishmaker:dish_add'), quasi_post_data)
        self.assertEquals(Dish.objects.count(), dish_count + 1)

    def test_order_creation_via_crud(self):
        orders_count = Order.objects.count()
        '''
            Get a list of ingredients from the dish to order
            ('cause orders are assembled from ingredients, that already persists in a dish)
        '''
        ingredients_dict = {ing.ingredient_id.name: ing.ingredient_quantity for ing in self.dish.dishrecipe.all()}

        quasi_post_data = {
            'another sample ingredient': ['3'],
            'Wotah': ['3'],
            'dish_id': self.dish.id,
            'description': ['sdsfds']
        }
        quasi_post_data.update(ingredients_dict)

        self.client.post(reverse('dishmaker:order_add'), quasi_post_data, pk=self.dish.id)
        self.assertEquals(Order.objects.count(), orders_count + 1)

    def test_order_fail_creation_via_crud(self):
        orders_count = Order.objects.count()
        print('order count:', orders_count)

        '''
            Get a list of ingredients from the dish to order, and choose their quantity
        '''
        ingredients_dict = {ing.ingredient_id.name: -20 for ing in self.dish.dishrecipe.all()}

        quasi_post_data = {
            'dish_id': self.dish.id,
            'description': ['sdsfds']
        }
        quasi_post_data.update(ingredients_dict)

        self.client.post(reverse('dishmaker:order_add'), quasi_post_data, dish_id=self.dish.id)
        self.assertEquals(Order.objects.count(), orders_count)

        ingredients_dict = {ing.ingredient_id.name: 0 for ing in self.dish.dishrecipe.all()}

        quasi_post_data = {
            'dish_id': self.dish.id,
            'description': ['sdsfds']
        }
        quasi_post_data.update(ingredients_dict)

        self.client.post(reverse('dishmaker:order_add'), quasi_post_data, dish_id=self.dish.id)
        self.assertEquals(Order.objects.count(), orders_count)
        print('order count after creation', Order.objects.count())

