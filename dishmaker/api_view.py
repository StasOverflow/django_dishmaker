from dishmaker.models import Order, Dish, Ingredient
from notes.models import NotedItem
from rest_framework import viewsets
from rest_framework import renderers
from rest_framework.decorators import detail_route
from rest_framework.response import Response
from rest_framework.generics import ListAPIView
from dishmaker.serializers import DishSerializer, IngredientsSerializer, OrderSerializer, NotedItemSerializer


class DishViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions.
    """
    queryset = Dish.objects.all()
    serializer_class = DishSerializer


class IngredientViewSet(viewsets.ModelViewSet):
    """
    Sample text on top
    """
    queryset = Ingredient.objects.all()
    serializer_class = IngredientsSerializer


class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer


class NoteViewSet(viewsets.ModelViewSet):
    queryset = NotedItem.objects.all()
    serializer_class = NotedItemSerializer

