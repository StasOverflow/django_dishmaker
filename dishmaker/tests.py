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

            'dishrecipe-0-ingredient_id': self.dish.dishrecipe.get(ingredient_id__name='cucumba').id,
            'dishrecipe-0-ingredient_quantity':
                self.dish.dishrecipe.get(ingredient_id__name='cucumba').ingredient_quantity,
            'dishrecipe-1-ingredient_id': self.dish.dishrecipe.get(ingredient_id__name='coconut').id,
            'dishrecipe-1-ingredient_quantity':
                self.dish.dishrecipe.get(ingredient_id__name='coconut').ingredient_quantity,
        }

        self.client.post(reverse('dishmaker:dish_add'), quasi_post_data)
        self.dish.dishrecipe.all()
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

    def test_ingredient_adding_via_crud(self):
        ingredient = Ingredient.objects.create(name='new', description='prev')

        quasi_post_data = {
            'name': self.dish.name,
            'description': self.dish.description,
            'dishrecipe-TOTAL_FORMS': ['3'],
            'dishrecipe-INITIAL_FORMS': ['1'],
            'dishrecipe-MIN_NUM_FORMS': ['1'],
            'dishrecipe-MAX_NUM_FORMS': ['1000'],

            'dishrecipe-0-ingredient_id': [str(Ingredient.objects.get(name='cucumba').id)],
            'dishrecipe-0-ingredient_quantity':
                [str(self.dish.dishrecipe.get(ingredient_id__name='cucumba').ingredient_quantity + 2)],
            'dishrecipe-0-id': [str(self.dish.dishrecipe.get(ingredient_id__name='cucumba').id)],
            'dishrecipe-0-dishrecipe_id': [str(self.dish.id)],

            'dishrecipe-1-ingredient_id': [str(Ingredient.objects.get(name='coconut').id)],
            'dishrecipe-1-ingredient_quantity':
                [str(self.dish.dishrecipe.get(ingredient_id__name='coconut').ingredient_quantity + 2)],
            'dishrecipe-1-id':  [str(self.dish.dishrecipe.get(ingredient_id__name='coconut').id)],
            'dishrecipe-1-dishrecipe_id': [str(self.dish.id)],

            'dishrecipe-2-ingredient_id': [str(Ingredient.objects.get(name='new').id)],
            'dishrecipe-2-ingredient_quantity': ['2'],
            'dishrecipe-2-id': [''],
            'dishrecipe-2-dishrecipe_id': [str(self.dish.id)],
        }

        count_before_creation = self.dish.dishrecipe.all().count()
        self.client.post(reverse('dishmaker:dish_update', kwargs={'pk': self.dish.id}), quasi_post_data)
        print(self.dish.dishrecipe.all().count())

        self.assertGreater(self.dish.dishrecipe.all().count(), count_before_creation)
