from django.urls import path

from .views import IndexView, DishView

app_name = 'dishmaker'

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('<int:dish_id>/', DishView.as_view(), name='dish'),
]
