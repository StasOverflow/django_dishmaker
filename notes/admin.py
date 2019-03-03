from django.contrib import admin
from .models import Note, NoteItem


class NoteAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'created_on')


class NoteItemAdmin(admin.ModelAdmin):
    list_display = ('note', 'content_type', 'object_id', 'content_object')


admin.site.register(Note, NoteAdmin)
admin.site.register(NoteItem, NoteItemAdmin)
