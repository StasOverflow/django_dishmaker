from django.shortcuts import render
from django.views.generic import TemplateView


class AizelParseView(TemplateView):
    template_name = "scrapy_aizel/index.html"
