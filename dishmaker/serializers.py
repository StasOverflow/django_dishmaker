from rest_framework import serializers
from dishmaker.models import Order, Dish, Ingredient
from notes.models import NotedItem
from rest_framework.serializers import RelatedField


class DishSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dish
        fields = ('name', 'description', 'ingredients', 'created_on', 'author')


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ('id', 'description', 'ingredients', 'created_on', 'author', 'is_active')


class IngredientsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ingredient
        fields = ('name', 'description', 'created_on')


class NotedItemSerializer(serializers.ModelSerializer):

    class NoteObjectRelatedField(serializers.RelatedField):

        def to_representation(self, value):
            if isinstance(value, Dish):
                return 'Bookmark: ' + value.name
            elif isinstance(value, Order):
                return 'Note: ' + str(value.id)
            raise Exception('Unexpected type of tagged object')

    content_object = NoteObjectRelatedField(read_only=True)

    class Meta:
        model = NotedItem
        fields = ('note', 'content_type', 'object_id', 'content_object', 'created_on')
