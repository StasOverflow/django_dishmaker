from dishmaker.models import Order, Dish, Ingredient
from notes.models import NotedItem
from rest_framework import viewsets
from rest_framework import renderers
from rest_framework.decorators import detail_route
from rest_framework.response import Response
from rest_framework.generics import ListAPIView
from rest_framework import permissions
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from dishmaker.permissions import IsOwnerOrReadOnly
from dishmaker.serializers import DishSerializer, IngredientsSerializer, OrderSerializer, NotedItemSerializer


class DishViewSet(viewsets.ModelViewSet):

    """
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions.
    """
    queryset = Dish.objects.all()
    serializer_class = DishSerializer
    permission_classes = (IsOwnerOrReadOnly, IsAuthenticated)


class IngredientViewSet(viewsets.ModelViewSet):

    """
    Sample text on top
    """
    queryset = Ingredient.objects.all()
    serializer_class = IngredientsSerializer
    permission_classes = (IsAuthenticatedOrReadOnly, )


class OrderViewSet(viewsets.ModelViewSet):

    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = (IsOwnerOrReadOnly, IsAuthenticated)


class NoteViewSet(viewsets.ModelViewSet):

    queryset = NotedItem.objects.all()
    serializer_class = NotedItemSerializer

