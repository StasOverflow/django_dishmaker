from django.shortcuts import render, reverse

from django.http import HttpResponse
from .models import DishRecipe
from django.views.generic import TemplateView
from django.views.generic import View
from django.views.generic.list import ListView
from django.views.generic.list import MultipleObjectMixin
from .models import DishRecipe


class BaseKindaAbstractView(MultipleObjectMixin):

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['list_views'] = ['Privetik']
        return context


class IndexView(ListView, BaseKindaAbstractView):
    template_name = "dishmaker/content/index.html"
    title = "Recipes list"
    model = DishRecipe

    def get_context_data(self, **kwargs):
        context = BaseKindaAbstractView.get_context_data(self, **kwargs)
        context['title'] = self.title
        # prefetch_related is like select_related, but for many to many cases
        recipes = DishRecipe.objects.prefetch_related('ingredients').all()
        context['recipes'] = recipes
        return context

        # return render(request, template_name=self.template_name, context={'title': self.title})
