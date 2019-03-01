from django.urls import path

from .views import IndexView, DishView, OrderView

app_name = 'dishmaker'

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('<int:dish_id>/', DishView.as_view(), name='dish'),
    path('order_page/<int:dish_id>', OrderView.as_view(), name='order'),
]
