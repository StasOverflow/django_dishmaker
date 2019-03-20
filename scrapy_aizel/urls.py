from django.urls import path
from scrapy_aizel.views import AizelParseView


app_name = 'scrapy_aizel'

urlpatterns = [
    path('', AizelParseView.as_view(), name='index'),
]
