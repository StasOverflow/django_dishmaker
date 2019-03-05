from django.contrib import admin
from .models import NotedItem


class NoteItemAdmin(admin.ModelAdmin):
    list_display = ('note', 'content_type', 'object_id', 'content_object', 'created_on')


admin.site.register(NotedItem, NoteItemAdmin)
