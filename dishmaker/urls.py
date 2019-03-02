from django.urls import path

from .views import DishListView, DishDetailView
from .views import IngredientListView, IngredientDetailView, IngredientCreateView
from .views import OrderView, OrderListView

app_name = 'dishmaker'

urlpatterns = [
    path('', DishListView.as_view(), name='index'),

    path('dish/<pk>/', DishDetailView.as_view(), name='dish'),

    path('order_page/<int:dish_id>', OrderView.as_view(), name='order'),
    path('order_list', OrderListView.as_view(), name='order_list'),

    path('ingredient/', IngredientListView.as_view(), name='ingredient_list'),
    path('ingredient/<pk>', IngredientDetailView.as_view(), name='ingredient'),
    path('ingredient/add/', IngredientCreateView.as_view(), name='ing_add'),
]
