from django.urls import reverse_lazy
from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import TemplateView
from django.views.generic.list import ListView
from django.views.generic.list import MultipleObjectMixin
from django.views.generic import CreateView
from django.views.generic import DetailView
from django.views.generic import UpdateView
from django.views.generic import DeleteView
from .models import Dish
from .models import Order
from .models import Ingredient
from .forms import DishIngredientFormSet
from django.db.models import Q

from .utils import many_to_many_igredients_get


class BaseKindaAbstractView(MultipleObjectMixin):

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['list_views'] = ['Privetik']
        return context


class DishListView(ListView, BaseKindaAbstractView):
    template_name = "dishmaker/content/index.html"
    title = "Recipes list"
    model = Dish

    def get_queryset(self):
        if self.request.method == 'GET':
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
            if dish is not None:

                dish_dict = dict()
                dish_dict['dish'] = dish
                dish_dict['ingredients'] = many_to_many_igredients_get(dish)
                recipe_list.append(dish_dict)

        context['recipes_list'] = recipe_list
        return context


class DishDetailView(DetailView):
    template_name = "dishmaker/content/dish_page.html"
    title = "A dish name"  # Should be replaced inside 'get_context_data' with a dish title
    model = Dish

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = self.object.name
        context['ingredients'] = many_to_many_igredients_get(self.object)

        return context


class DishCreateView(CreateView):
    model = Dish
    title = "Add a Dish"
    fields = ['name', 'description']
    success_url = reverse_lazy('dishmaker:index')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = self.title
        if self.request.POST:
            # print('GOT POST with ', self.request.POST)
            if self.object is not None:
                context['dish_formset'] = DishIngredientFormSet(self.request.POST)
            else:
                context['dish_formset'] = DishIngredientFormSet()

            print(self.request.POST)
        else:
            context['dish_formset'] = DishIngredientFormSet()
        return context

    def form_valid(self, form):
        context = self.get_context_data()
        formset = context['dish_formset']

        if self.object:
            form.save()

        if formset.is_valid():
            formset.instance = self.object
            formset.save()

        return super().form_valid(form)


class DishUpdateView(UpdateView):
    model = Dish
    title = "Add a Dish"
    fields = ['name', 'description']
    success_url = reverse_lazy('dishmaker:index')

    def get_context_data(self, **kwargs):
        context = super(DishUpdateView, self).get_context_data(**kwargs)
        if self.request.POST:
            context['dish_formset'] = DishIngredientFormSet(self.request.POST, instance=self.object)
        else:
            context['dish_formset'] = DishIngredientFormSet(instance=self.object)
        return context

    def form_valid(self, form):
        context = self.get_context_data()
        formset = context['dish_formset']

        if formset.is_valid():
            formset.instance = self.object
            formset.save()

        return super().form_valid(form)


class DishDeleteView(DeleteView):
    model = Dish
    title = "Remove dish"
    success_url = reverse_lazy('dishmaker:index')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = self.title
        return context


class IngredientListView(ListView, BaseKindaAbstractView):
    template_name = "dishmaker/content/ingredient_list.html"
    title = "Ingredient list"
    model = Ingredient

    def get_context_data(self, **kwargs):
        context = BaseKindaAbstractView.get_context_data(self, **kwargs)
        context['title'] = self.title
        context['ingredients'] = self.object_list
        return context


class IngredientDetailView(DetailView):
    template_name = "dishmaker/content/ingredient_page.html"
    model = Ingredient

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = self.object.name
        # context['categories'] = list_categories(storeId)
        return context


class IngredientCreateView(CreateView):
    model = Ingredient
    title = "Add Ingredient"
    fields = ['name', 'description']
    success_url = reverse_lazy('dishmaker:ingredient_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = self.title
        return context


class IngredientUpdateView(UpdateView):
    model = Ingredient
    title = "Update Ingredient"
    fields = ['name', 'description']
    success_url = reverse_lazy('dishmaker:ingredient_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = self.title
        return context


class IngredientDeleteView(DeleteView):
    model = Ingredient
    title = "Remove ingredient"
    success_url = reverse_lazy('dishmaker:ingredient_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = self.title
        return context


class OrderView(TemplateView, BaseKindaAbstractView):
    template_name = "dishmaker/content/order_page.html"
    title = "A dish name"   # Should be replaced inside 'get_context_data' with a dish title
    model = Dish

    def post(self, request, *args, **kwargs):
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
