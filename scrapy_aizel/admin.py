from .models import AizelClothItem, Size
from django.contrib import admin


# class ClotItemAdmin(admin.ModelAdmin):
#     list_display = ('title', 'price', 'size')


admin.site.register(AizelClothItem)
admin.site.register(Size)