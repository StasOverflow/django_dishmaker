from django.contrib import admin
from .models import Dish, Ingredient, Order


class DishRecipeIngredientInline(admin.TabularInline):
    model = Dish.ingredients.through
    verbose_name = 'Ingredient to your recipe'
    fields = ['ingredient_id', 'ingredient_quantity', ]
    extra = 1


class OrderIngredientInline(admin.TabularInline):
    model = Dish.ingredients.through
    verbose_name = 'Ingredient to your recipe'
    fields = ['ingredient_id', 'ingredient_quantity', ]
    extra = 0


class DishAdmin(admin.ModelAdmin):
    inlines = [
        DishRecipeIngredientInline,
    ]
    list_display = ('name', 'description', 'author')


class IngredientAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')


class OrderAdmin(admin.ModelAdmin):
    inlines = [
        OrderIngredientInline,
    ]
    list_display = ('id', 'description', 'author', 'is_active')


admin.site.register(Dish, DishAdmin)
admin.site.register(Ingredient, IngredientAdmin)
admin.site.register(Order, OrderAdmin)
