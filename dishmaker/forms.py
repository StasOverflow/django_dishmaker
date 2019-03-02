from django import forms
from .models import Dish
from .models import Order
from .models import Ingredient
from .models import IngredientQuantityInDishProxy
from django.forms import inlineformset_factory
from django.forms import ModelForm


class DishForm(ModelForm):

    class Meta:
        model = Dish
        fields = ('name', 'description')


DishIngredientFormSet = inlineformset_factory(
                            Dish, IngredientQuantityInDishProxy,
                            fields=['ingredient_id', 'ingredient_quantity'],
                            extra=2,
                            form=DishForm
                        )


class OrderForm(ModelForm):

    class Meta:
        model = Order
        fields = ('dish_id', 'description')


OrderIngredientFormSet = inlineformset_factory(
                            Order, IngredientQuantityInDishProxy,
                            fields=['ingredient_id', 'ingredient_quantity'],
                            extra=0,
                            form=OrderForm
                        )
