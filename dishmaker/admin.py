from django.contrib import admin

# Register your models here.
from .models import DishRecipe, Ingredient, Order


class DishAdmin(admin.ModelAdmin):
    # exclude = ('updated_on',)
    # list_display = ('title', 'created_on',)
    # list_filter = ('created_on', 'title', )
    list_display = ('name', )


class IngredientAdmin(admin.ModelAdmin):
    list_display = ('name', )
    # exclude = ('meta_keywords',)
    # list_display = ('name', 'is_active', 'description')
    # list_filter = ('description', 'name', )


admin.site.register(DishRecipe, DishAdmin)
admin.site.register(Ingredient, IngredientAdmin)
