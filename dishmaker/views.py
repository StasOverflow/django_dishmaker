from django.urls import reverse_lazy
from django.http import HttpResponse
from django.shortcuts import redirect
from django.shortcuts import reverse
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
from .forms import OrderIngredientFormSet
from django.http import HttpResponseRedirect
from django.db.models import Q
from .utils import many_to_many_igredients_get
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.mixins import PermissionRequiredMixin


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
        context['model_type'] = self.model.__name__

        return context


class DishCreateView(PermissionRequiredMixin, LoginRequiredMixin, CreateView):

    permission_required = ("is_staff", "is_superuser", )

    model = Dish
    title = "Add a Dish"
    fields = ['name', 'description']
    success_url = reverse_lazy('dishmaker:index')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.object = None

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = self.title
        if self.request.POST:
            # print(self.request.POST)
            context['dish_formset'] = DishIngredientFormSet(self.request.POST)
        else:
            context['dish_formset'] = DishIngredientFormSet()
        return context

    def form_valid(self, form):
        context = self.get_context_data()
        formset = context['dish_formset']

        if form.is_valid():

            if formset.is_valid():
                self.object = form.save()
                formset.instance = self.object
                formset.save()
                return super().form_valid(form)
            else:
                return redirect(reverse('dishmaker:dish_add'))


class DishUpdateView(PermissionRequiredMixin, LoginRequiredMixin, UpdateView):

    permission_required = ("is_staff", "is_superuser", )

    model = Dish
    title = "Update a Dish"
    fields = ['name', 'description']
    success_url = reverse_lazy('dishmaker:index')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
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


class DishDeleteView(PermissionRequiredMixin, LoginRequiredMixin, DeleteView):

    permission_required = ("is_staff", "is_superuser", )

    model = Dish
    title = "Remove dish"
    success_url = reverse_lazy('dishmaker:index')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = self.title
        return context


class IngredientListView(PermissionRequiredMixin, LoginRequiredMixin, ListView, BaseKindaAbstractView):

    permission_required = ("is_staff", "is_superuser", )

    template_name = "dishmaker/content/ingredient_list.html"
    title = "Ingredient list"
    model = Ingredient

    def get_context_data(self, **kwargs):
        context = BaseKindaAbstractView.get_context_data(self, **kwargs)
        context['title'] = self.title
        context['ingredients'] = self.object_list
        return context


class IngredientDetailView(PermissionRequiredMixin, LoginRequiredMixin, DetailView):

    permission_required = ("is_staff", "is_superuser", )

    template_name = "dishmaker/content/ingredient_page.html"
    model = Ingredient

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = self.object.name
        # context['categories'] = list_categories(storeId)
        return context


class IngredientCreateView(PermissionRequiredMixin, LoginRequiredMixin, CreateView):

    permission_required = ("is_staff", "is_superuser", )

    model = Ingredient
    title = "Add Ingredient"
    fields = ['name', 'description']
    success_url = reverse_lazy('dishmaker:ingredient_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = self.title
        return context


class IngredientUpdateView(PermissionRequiredMixin, LoginRequiredMixin, UpdateView):

    permission_required = ("is_staff", "is_superuser", )

    model = Ingredient
    title = "Update Ingredient"
    fields = ['name', 'description']
    success_url = reverse_lazy('dishmaker:ingredient_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = self.title
        return context


class IngredientDeleteView(PermissionRequiredMixin, LoginRequiredMixin, DeleteView):

    permission_required = ("is_staff", "is_superuser", )

    model = Ingredient
    title = "Remove ingredient"
    success_url = reverse_lazy('dishmaker:ingredient_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = self.title
        return context


class OrderDetailView(LoginRequiredMixin, DetailView):
    template_name = "dishmaker/content/order_page.html"
    title = "A dish name"   # Should be replaced inside 'get_context_data' with a dish title
    model = Order

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Order: ' + str(self.object.id)
        '''
            In case there will be repetitions of ingredients, we need to split procedure into two parts
        '''
        ing_list = [
            (ing.ingredient_id.name, ing.ingredient_quantity) for ing in self.object.order.all()
        ]
        context['ingredients'] = dict()
        context['model_type'] = self.model.__name__
        for ing in ing_list:
            if ing[0] not in context['ingredients']:
                value = ing[1]
            else:
                value = context['ingredients'][ing[0]] + ing[1]
            context['ingredients'][ing[0]] = value

        return context


class OrderFromDish(LoginRequiredMixin, TemplateView):
    template_name = "dishmaker/content/order_from_dish.html"
    title = "A dish name"   # Should be replaced inside 'get_context_data' with a dish title
    model = Dish

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
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


class OrderCreateView(LoginRequiredMixin, TemplateView):
    model = Order
    success_url = reverse_lazy('dishmaker:order_list')

    blacklist = ('csrfmiddlewaretoken', 'description', 'dish_id')

    def post(self, request, *args, **kwargs):
        ingredient_dict = {key: value for key, value in request.POST.items() if key not in self.blacklist}

        for value in ingredient_dict.values():
            if int(value) < 1:
                error_message = 'ingredient quantity cant be lower than 1'
                data = dict()
                data.update(request.POST)
                data['error_message'] = error_message
                return redirect(reverse('dishmaker:order_from_dish',
                                        kwargs={'dish_id': request.POST.get('dish_id')}),
                                )

        instance = self.model.objects.create(dish_id=Dish.objects.get(pk=request.POST.get('dish_id')),
                                             description=request.POST.get('description'))

        for ingred, quantity in ingredient_dict.items():
            ingredient_database_instance = Ingredient.objects.filter(name=ingred).first()
            '''order here is a related name'''
            instance.order.create(ingredient_id=ingredient_database_instance, ingredient_quantity=quantity)

        return redirect(self.success_url)


class OrderListView(LoginRequiredMixin, ListView, BaseKindaAbstractView):
    template_name = "dishmaker/content/order_list.html"
    title = "Order list"
    model = Order

    def get_context_data(self, **kwargs):
        context = BaseKindaAbstractView.get_context_data(self, **kwargs)
        context['title'] = self.title
        orders = self.object_list
        order_list = list()

        for order in orders:
            if order is not None:

                order_dict = dict()
                order_dict['order'] = order
                order_dict['ingredients'] = dict()
                ing_list = [
                    (
                        ing.ingredient_id.name,
                        ing.ingredient_quantity
                    ) for ing in order.order.all() if ing.ingredient_id is not None
                ]
                for ing in ing_list:
                    if ing[0] not in order_dict['ingredients']:
                        value = ing[1]
                    else:
                        value = order_dict['ingredients'][ing[0]] + ing[1]
                    order_dict['ingredients'][ing[0]] = value

                order_list.append(order_dict)

        context['order_list'] = order_list
        return context


class OrderDeleteView(PermissionRequiredMixin, LoginRequiredMixin, DeleteView):

    permission_required = ("is_staff", "is_superuser", )

    model = Order
    title = "Remove an order"
    success_url = reverse_lazy('dishmaker:order_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = self.title
        return context


class OrderUpdateView(PermissionRequiredMixin, LoginRequiredMixin, UpdateView):

    permission_required = ("is_staff", "is_superuser", )

    model = Order
    title = "Update an order"
    success_url = reverse_lazy('dishmaker:order_list')
    fields = ['dish_id', 'description']

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.POST:
            context['order_formset'] = OrderIngredientFormSet(self.request.POST, instance=self.object)
        else:
            context['order_formset'] = OrderIngredientFormSet(instance=self.object)
        return context

    def form_valid(self, form):
        context = self.get_context_data()
        formset = context['order_formset']

        if formset.is_valid():
            formset.instance = self.object
            formset.save()

        return super().form_valid(form)

