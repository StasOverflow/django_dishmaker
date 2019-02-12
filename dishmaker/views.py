from django.shortcuts import render, reverse

from django.http import HttpResponse

from django.views.generic import TemplateView


class IndexView(TemplateView):
    template_name = "dishmaker/index.html"
