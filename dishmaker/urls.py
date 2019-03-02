from django.urls import path

from .views import DishListView
from .views import DishDetailView, DishDeleteView, DishCreateView, DishUpdateView
from .views import IngredientListView
from .views import IngredientDetailView, IngredientCreateView, IngredientUpdateView, IngredientDeleteView
from .views import OrderView, OrderListView

app_name = 'dishmaker'

urlpatterns = [
    path('', DishListView.as_view(), name='index'),
    path('dish/<pk>/', DishDetailView.as_view(), name='dish_page'),
    path('dish_add/add/', DishCreateView.as_view(), name='dish_add'),       # Having an issue when using 'dish/add/
    path('dish/update/<pk>/', DishUpdateView.as_view(), name='dish_update'),
    path('dish/delete/<pk>/', DishDeleteView.as_view(), name='dish_delete'),

    path('order_page/<int:dish_id>', OrderView.as_view(), name='order'),
    path('order_list', OrderListView.as_view(), name='order_list'),

    path('ingredient/', IngredientListView.as_view(), name='ingredient_list'),
    path('ingredient/<pk>', IngredientDetailView.as_view(), name='ingredient'),
    path('ingredient/add/', IngredientCreateView.as_view(), name='ing_add'),
    path('ingredient/update/<pk>/', IngredientUpdateView.as_view(), name='ing_update'),
    path('ingredient/delete/<pk>/', IngredientDeleteView.as_view(), name='ing_delete'),
]
