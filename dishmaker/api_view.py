from dishmaker.models import Order, Dish, Ingredient
from notes.models import NotedItem
from rest_framework.generics import ListAPIView
from dishmaker.serializers import DishSerializer, IngredientsSerializer, OrderSerializer, NotedItemSerializer


class DishList(ListAPIView):
    queryset = Dish.objects.all()
    serializer_class = DishSerializer


class IngredientsList(ListAPIView):
    queryset = Ingredient.objects.all()
    serializer_class = IngredientsSerializer


class OrderList(ListAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer


class NotesList(ListAPIView):
    queryset = NotedItem.objects.all()
    serializer_class = NotedItemSerializer
