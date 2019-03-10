from rest_framework import serializers
from dishmaker.models import Order, Dish, Ingredient, IngredientQuantityInDishProxy
from notes.models import NotedItem
from rest_framework.serializers import RelatedField
from django.contrib.auth.models import User


class IngredientsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ingredient
        fields = ('id', 'name', 'description', 'created_on')


class IngredientQuantitySerializer(serializers.HyperlinkedModelSerializer):

    name = serializers.CharField(source='ingredient_id.name')

    class Meta:
        model = IngredientQuantityInDishProxy

        fields = ('id', 'name', 'ingredient_quantity')


class AuthorRelatedField(RelatedField):

    def to_representation(self, value):
        return value.username

    def to_internal_value(self, data):
        return User.objects.get(username=data)


class DishSerializer(serializers.ModelSerializer):

    ingredients = IngredientQuantitySerializer(source='dishrecipe', many=True)
    author = AuthorRelatedField(queryset=User.objects.all())

    class Meta:
        model = Dish
        fields = ('id', 'name', 'description', 'ingredients', 'created_on', 'author')

    def create(self, validated_data):
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

    ingredients = IngredientQuantitySerializer(source='order', many=True)
    dish_id = serializers.PrimaryKeyRelatedField(source='dish_id.name', queryset=Dish.objects.all())

    author = AuthorRelatedField(queryset=User.objects.all())

    class Meta:
        model = Order
        fields = ('id', 'dish_id', 'description', 'ingredients', 'created_on', 'author', 'is_active')

    def create(self, validated_data):
        ings_data = validated_data.pop('dishrecipe')
        order = Order.objects.create(**validated_data)
        for ing in ings_data:
            name = ing.get('ingredient_id').get('name')
            quantity = ing.get('ingredient_quantity')
            ingredient_database_instance = Ingredient.objects.filter(name=name).first()
            '''order here is a related name'''
            order.order.create(ingredient_id=ingredient_database_instance,
                               ingredient_quantity=quantity)
        return order


class ContentTypeField(serializers.RelatedField):

    def to_representation(self, value):
        if isinstance(value, Dish):
            return 'Dish: ' + value.name
        elif isinstance(value, Order):
            return 'Order: ' + str(value.id)
        raise Exception('Unexpected type of tagged object')


class NotedItemSerializer(serializers.ModelSerializer):

    class NoteObjectRelatedField(serializers.RelatedField):

        def to_representation(self, value):
            if isinstance(value, Dish):
                return DishSerializer(value).data
            elif isinstance(value, Order):
                return OrderSerializer(value).data
            raise Exception('Unexpected type of tagged object')

    content_object = NoteObjectRelatedField(read_only=True)

    class Meta:
        model = NotedItem
        fields = ('id', 'note', 'content_type', 'object_id', 'content_object', 'created_on')
