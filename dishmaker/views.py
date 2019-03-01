from django.shortcuts import render, reverse

from django.http import HttpResponse
from .models import DishRecipe
from django.views.generic import TemplateView
from django.views.generic import View
from django.views.generic.list import ListView
from django.views.generic.list import MultipleObjectMixin
from .models import DishRecipe


class BaseKindaAbstractView(MultipleObjectMixin):

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['list_views'] = ['Privetik']
        return context


class IndexView(ListView, BaseKindaAbstractView):
    template_name = "dishmaker/content/index.html"
    title = "Recipes list"
    model = DishRecipe

    def get_context_data(self, **kwargs):
        context = BaseKindaAbstractView.get_context_data(self, **kwargs)
        context['title'] = self.title
        recipes = DishRecipe.objects.prefetch_related('ingredients').all()
        context['recipes'] = recipes
        return context


class DishView(ListView, BaseKindaAbstractView):
    template_name = "dishmaker/content/dish_page.html"
    title = "A dish name"   # Should be replaced inside 'get_context_data' with a dish title
    model = DishRecipe

    def get_context_data(self, **kwargs):
        context = BaseKindaAbstractView.get_context_data(self, **kwargs)
        if 'dish_id' in self.kwargs:
            dish = self.model.objects.filter(id=self.kwargs['dish_id']).first()
            context['title'] = dish.name
            context['description'] = dish.description
            '''
                In case there will be repetitions of ingredients, we need to split procedure into two parts
            '''
            ing_list = [
                (ing.ingredient_id.name, ing.ingredient_quantity) for ing in dish.dishrecipe.all()
            ]
            context['ingredients'] = dict()
            for ing in ing_list:
                if ing[0] not in context['ingredients']:
                    value = ing[1]
                else:
                    value = context['ingredients'][ing[0]] + ing[1]
                context['ingredients'][ing[0]] = value

            context['dish_id'] = self.kwargs['dish_id']

        return context


class OrderView(ListView, BaseKindaAbstractView):
    template_name = "dishmaker/content/order_page.html"
    title = "A dish name"   # Should be replaced inside 'get_context_data' with a dish title
    model = DishRecipe

    def get_context_data(self, **kwargs):
        context = BaseKindaAbstractView.get_context_data(self, **kwargs)
        if 'dish_id' in self.kwargs:
            dish = self.model.objects.filter(id=self.kwargs['dish_id']).first()
            context['title'] = dish.name + ' order'
            context['description'] = dish.description
            '''
                In case there will be repetitions of ingredients, we need to split procedure into two parts
            '''
            ing_list = [
                (ing.ingredient_id.name, ing.ingredient_quantity) for ing in dish.dishrecipe.all()
            ]
            context['ingredients'] = dict()
            for ing in ing_list:
                if ing[0] not in context['ingredients']:
                    value = ing[1]
                else:
                    value = context['ingredients'][ing[0]] + ing[1]
                context['ingredients'][ing[0]] = value

        return context
