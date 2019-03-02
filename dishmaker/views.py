from django.shortcuts import render, reverse
from django.http import HttpResponse
from .models import Dish
from django.views.generic import TemplateView
from django.views.generic import View
from django.views.generic.list import ListView
from django.views.generic.list import MultipleObjectMixin
from .models import Dish
from .models import Order
from .forms import OrderForm
from django.db.models import Q


class BaseKindaAbstractView(MultipleObjectMixin):

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['list_views'] = ['Privetik']
        return context


class IndexView(ListView, BaseKindaAbstractView):
    template_name = "dishmaker/content/index.html"
    title = "Recipes list"
    model = Dish

    def get_queryset(self):
        if self.request.method == 'GET':
            print('having GET ', self.request.GET)
            if 'search' in self.request.GET:
                searchword = self.request.GET.get('search')
                filter_criteria = Q(name__icontains=searchword) | Q(description__icontains=searchword)
                queryset = self.model.objects.filter(filter_criteria).prefetch_related('ingredients')
            else:
                queryset = self.model.objects.all().prefetch_related('ingredients')
        return queryset

    def get_context_data(self, **kwargs):
        context = BaseKindaAbstractView.get_context_data(self, **kwargs)
        context['title'] = self.title
        recipes = self.object_list
        recipe_list = list()

        for dish in recipes:
            dish_dict = dict()
            dish_dict['dish'] = dish
            '''
                In case there will be repetitions of ingredients, we need to split procedure into two parts
            '''
            ing_list = [
                (ing.ingredient_id.name, ing.ingredient_quantity) for ing in dish.dishrecipe.all()
            ]
            dish_dict['ingredients'] = dict()
            for ing in ing_list:
                if ing[0] not in dish_dict['ingredients']:
                    value = ing[1]
                else:
                    value = dish_dict['ingredients'][ing[0]] + ing[1]
                dish_dict['ingredients'][ing[0]] = value
            recipe_list.append(dish_dict)

        context['recipes_list'] = recipe_list
        print(context)
        return context


class DishView(ListView, BaseKindaAbstractView):
    template_name = "dishmaker/content/dish_page.html"
    title = "A dish name"   # Should be replaced inside 'get_context_data' with a dish title
    model = Dish

    def get_context_data(self, **kwargs):
        print(kwargs)
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


class OrderView(TemplateView, BaseKindaAbstractView):
    template_name = "dishmaker/content/order_page.html"
    title = "A dish name"   # Should be replaced inside 'get_context_data' with a dish title
    model = Dish

    def post(self, request, *args, **kwargs):
        print(request.POST)
        print(kwargs)
        return HttpResponse('We will create an order, somewhen..')

    def get_context_data(self, **kwargs):
        context = dict()
        # context = BaseKindaAbstractView.get_context_data(self, **kwargs)
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


class OrderListView(ListView, BaseKindaAbstractView):
    template_name = "dishmaker/content/order_page.html"
    title = "Order list"
    model = Order
    http_method_names = ['post']

    def get_context_data(self, **kwargs):
        context = BaseKindaAbstractView.get_context_data(self, **kwargs)
        context['title'] = self.title
        recipes = self.objects.prefetch_related('ingredients').all()
        context['recipes'] = recipes
        return context
