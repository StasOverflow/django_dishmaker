from django.urls import path
from .views import NoteListView, NoteCreateView


app_name = 'notes'

urlpatterns = [
    path('', NoteListView.as_view(), name='index'),
    path('create_note/', NoteCreateView.as_view(), name='create_note'),
]
