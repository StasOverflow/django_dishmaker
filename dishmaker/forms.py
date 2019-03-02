from django import forms
from .models import Dish
from .models import Order
from .models import Ingredient
from .models import IngredientQuantityInDishProxy
from django.forms import inlineformset_factory
from django.forms import BaseModelFormSet
from django.forms import ModelForm


class DishForm(ModelForm):

    class Meta:
        model = Dish
        fields = ('name', 'description')


DishIngredientFormSet = inlineformset_factory(
                            Dish, IngredientQuantityInDishProxy,
                            fields=['ingredient_id', 'ingredient_quantity'],
                            extra=1,
                            form=DishForm
                        )


# class AdditionalIngredient(BaseModelFormSet):
#
#     ingredients_choice = forms.ModelMultipleChoiceField(queryset=Dish.dishrecipe.all())

    # class Meta:
    #     model = Order
    #     fields = ['ingredients_choice']


'''

class PizzaForm(ModelForm):
    class Meta:
        model = Order

    # Representing the many to many related field in Pizza
    # toppings = ModelMultipleChoiceField(queryset=Topping.objects.all())

    # Overriding __init__ here allows us to provide initial
    # data for 'toppings' field
    def __init__(self, *args, **kwargs):
        ModelForm.__init__(self, *args, **kwargs)
        print(args, kwargs)
        # Only in case we build the form from an instance
        # (otherwise, 'toppings' list should be empty)
        # if kwargs.get('instance'):
        #     # We get the 'initial' keyword argument or initialize it
        #     # as a dict if it didn't exist.
        #     initial = kwargs.setdefault('initial', {})
        #     # The widget for a ModelMultipleChoiceField expects
        #     # a list of primary key for the selected data.
        #     initial['toppings'] = [t.pk for t in kwargs['instance'].topping_set.all()]
        #

    # Overriding save allows us to process the value of 'toppings' field
    def save(self, commit=True):
        pass
        # Get the unsave Pizza instance
        # instance = ModelForm.save(self, False)
        #
        # Prepare a 'save_m2m' method for the form,
        # old_save_m2m = self.save_m2m
        #
        # def save_m2m():
        #    old_save_m2m()
        #    # This is where we actually link the pizza with toppings
        #    instance.topping_set.clear()
        #    instance.topping_set.add(*self.cleaned_data['toppings'])
        # self.save_m2m = save_m2m

        # Do we need to save all changes now?
        # if commit:
        #     instance.save()
        #     self.save_m2m()
        #
        # return in
'''
