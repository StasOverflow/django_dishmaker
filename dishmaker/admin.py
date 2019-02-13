from django.contrib import admin

# Register your models here.
from .models import DishRecipe, Ingredient, Order, IngredientQuantityInDishProxy


class DishRecipeIngredientInline(admin.TabularInline):
    model = DishRecipe.ingredients.through
    verbose_name = 'Ingredient to your recipe'
    fields = ['ingredient_id', 'ingredient_quantity', ]
    extra = 1


class DishAdmin(admin.ModelAdmin):
    inlines = [
        DishRecipeIngredientInline,
    ]
    list_display = ('name', 'description')


class IngredientAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')


admin.site.register(DishRecipe, DishAdmin)
admin.site.register(Ingredient, IngredientAdmin)
