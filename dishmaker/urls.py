from django.urls import path

from .views import DishListView
from .views import DishDetailView, DishDeleteView, DishCreateView, DishUpdateView
from .views import IngredientListView
from .views import IngredientDetailView, IngredientCreateView, IngredientUpdateView, IngredientDeleteView
from .views import OrderListView
from .views import OrderDetailView, OrderCreateView, OrderFromDish, OrderDeleteView, OrderUpdateView

from rest_framework import routers
from dishmaker.api_view import DishViewSet, NoteViewSet, OrderViewSet, IngredientViewSet


app_name = 'dishmaker'

router = routers.SimpleRouter()
router.register(r'api_dishes', DishViewSet)
router.register(r'api_notes', NoteViewSet)
router.register(r'api_ingredients', IngredientViewSet)
router.register(r'api_orders', OrderViewSet)

urlpatterns = [
    path('', DishListView.as_view(), name='index'),
    path('dish/<pk>/', DishDetailView.as_view(), name='dish_page'),
    path('dish_add/add/', DishCreateView.as_view(), name='dish_add'),       # Having an issue when using 'dish/add/
    path('dish/update/<pk>/', DishUpdateView.as_view(), name='dish_update'),
    path('dish/delete/<pk>/', DishDeleteView.as_view(), name='dish_delete'),

    path('form_an_order/<int:dish_id>', OrderFromDish.as_view(), name='order_from_dish'),

    path('order_list/', OrderListView.as_view(), name='order_list_page'),
    path('order_page/<pk>', OrderDetailView.as_view(), name='order_page'),
    path('order_page/add/', OrderCreateView.as_view(), name='order_add'),
    path('order_page/update/<pk>', OrderUpdateView.as_view(), name='order_update'),
    path('order_page/delete/<pk>', OrderDeleteView.as_view(), name='order_delete'),

    path('ingredient/', IngredientListView.as_view(), name='ingredient_list_page'),
    path('ingredient/<pk>', IngredientDetailView.as_view(), name='ingredient'),
    path('ingredient/add/', IngredientCreateView.as_view(), name='ing_add'),
    path('ingredient/update/<pk>/', IngredientUpdateView.as_view(), name='ing_update'),
    path('ingredient/delete/<pk>/', IngredientDeleteView.as_view(), name='ing_delete'),
]

urlpatterns += router.urls
