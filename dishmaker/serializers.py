from rest_framework import serializers
from dishmaker.models import Order, Dish, Ingredient, IngredientQuantityInDishProxy
from notes.models import NotedItem
from rest_framework.serializers import RelatedField


class IngredientsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ingredient
        fields = ('name', 'description', 'created_on')


class IngredientQuantitySerializer(serializers.HyperlinkedModelSerializer):

    name = serializers.CharField(source='ingredient_id.name')

    class Meta:
        model = IngredientQuantityInDishProxy

        fields = ('name', 'ingredient_quantity')


class DishSerializer(serializers.ModelSerializer):
    ingredients = IngredientQuantitySerializer(source='dishrecipe', many=True)

    class Meta:
        model = Dish
        fields = ('name', 'description', 'ingredients', 'created_on', 'author')

    def create(self, validated_data):
        print(validated_data )
        ings_data = validated_data.pop('dishrecipe')
        dish = Dish.objects.create(**validated_data)
        for ing in ings_data:
            name = ing.get('ingredient_id').get('name')
            quantity = ing.get('ingredient_quantity')
            ingredient_database_instance = Ingredient.objects.filter(name=name).first()
            '''order here is a related name'''
            dish.dishrecipe.create(ingredient_id=ingredient_database_instance,
                                   ingredient_quantity=quantity)
        return dish


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ('id', 'description', 'ingredients', 'created_on', 'author', 'is_active')


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