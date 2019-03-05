from django.shortcuts import render, redirect, reverse
from django.urls import reverse_lazy
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic.list import ListView
from django.views.generic import CreateView, DetailView, TemplateView
from .models import Note
from django.apps.registry import apps


class NoteListView(ListView):
    model = Note
    title = 'Note list'
    template_name = 'notes/note_list.html'

    def get_context_data(self, **kwargs):
        context = super(NoteListView, self).get_context_data()
        context['title'] = self.title
        return context


class NotePreCreateView(TemplateView):
    template_name = "notes/note_page.html"
    title = "A dish name"   # Should be replaced inside 'get_context_data' with a dish title
    model = Note

    def post(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        model = apps.get_model('dishmaker', request.POST.get('model_name'))
        model_id = request.POST.get('model_id')

        print(model)
        return self.render_to_response(context)

    def get(self, request, *args, **kwargs):
        # context = self.get_context_data(**kwargs)
        url = reverse('notes:index')
        return HttpResponseRedirect(url)

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        # if self.model_to_add_name is not None:

            # dish = self.model.objects.filter(id=self.kwargs['dish_id']).first()
            # context['title'] = dish.name
            # context['description'] = dish.description
            # '''
            #     In case there will be repetitions of ingredients, we need to split procedure into two parts
            # '''
            # ing_list = [
            #     (ing.ingredient_id.name, ing.ingredient_quantity) for ing in dish.dishrecipe.all()
            # ]
            # context['ingredients'] = dict()
            # for ing in ing_list:
            #     if ing[0] not in context['ingredients']:
            #         value = ing[1]
            #     else:
            #         value = context['ingredients'][ing[0]] + ing[1]
            #     context['ingredients'][ing[0]] = value
            #
            # context['dish_id'] = self.kwargs['dish_id']

        return context


class NoteCreateView(TemplateView):
    model = Note
    success_url = reverse_lazy('notes:index')

    def post(self, request, *args, **kwargs):
        print(request.POST)

        return redirect(self.success_url)


class OrderCreateView(TemplateView):
    pass
    # model = OrderCreateView
    # success_url = reverse_lazy('dishmaker:order_list')
    #
    # blacklist = ('csrfmiddlewaretoken', 'description', 'dish_id')
    #
    # def post(self, request, *args, **kwargs):
    #     instance = self.model.objects.create(dish_id=Dish.objects.get(pk=request.POST.get('dish_id')),
    #                                          description=request.POST.get('description'))
    #     ingredient_dict = {key: value for key, value in request.POST.items() if key not in self.blacklist}
    #     instance.save()
    #
    #     for ingred, quantity in ingredient_dict.items():
    #         ingredient_database_instance = Ingredient.objects.filter(name=ingred).first()
    #         instance.order.create(ingredient_id=ingredient_database_instance, ingredient_quantity=quantity)
    #
    #     return redirect(self.success_url)





#     title = "Add a Dish"
#     fields = ['name', 'description']
#     success_url = reverse_lazy('dishmaker:index')
#
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['title'] = self.title
#         if self.request.POST:
#             # print('GOT POST with ', self.request.POST)
#             context['dish_formset'] = DishIngredientFormSet(self.request.POST)
#         else:
#             context['dish_formset'] = DishIngredientFormSet()
#         return context
#
#     def form_valid(self, form):
#         context = self.get_context_data()
#         formset = context['dish_formset']
#
#         self.object = form.save()
#
#         if formset.is_valid():
#             formset.instance = self.object
#             formset.save()
#
#         return super().form_valid(form)