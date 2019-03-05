from django.urls import path
from .views import NoteOrderListView, NoteDishListView, NoteCreateView


app_name = 'notes'

urlpatterns = [
    path('order_notes/', NoteOrderListView.as_view(), name='order_notes'),
    path('dish_notes/', NoteDishListView.as_view(), name='dish_notes'),
    path('create_note/', NoteCreateView.as_view(), name='create_note'),
]
