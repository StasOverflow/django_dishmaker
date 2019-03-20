from django.urls import path
from scrapy_aizel.views import AizelParseView, AizelListView


app_name = 'scrapy_aizel'

urlpatterns = [
    path('', AizelParseView.as_view(), name='index'),
    path('clothes_view/', AizelListView.as_view(), name='clothes_list_view'),
]
