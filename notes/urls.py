from django.urls import path
from .views import NoteListView, NotePreCreateView, NoteCreateView


app_name = 'notes'

urlpatterns = [
    path('', NoteListView.as_view(), name='index'),
    path('create_note/', NotePreCreateView.as_view(), name='create_note'),
    path('hidden_create_note/', NoteCreateView.as_view(), name='hidden_create_note'),
]
