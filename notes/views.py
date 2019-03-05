from django.shortcuts import render, redirect, reverse
from django.urls import reverse_lazy
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic.list import ListView
from django.views.generic import CreateView, DetailView, TemplateView
from .models import NotedItem
from django.apps.registry import apps
from .forms import NoteForm


class NoteListView(ListView):
    model = NotedItem
    title = 'Note list'
    template_name = 'notes/note_list.html'

    def get_context_data(self, **kwargs):
        context = super(NoteListView, self).get_context_data()
        context['title'] = self.title
        return context


class NoteCreateView(TemplateView):
    template_name = "notes/note_page.html"
    title = ""
    model = NotedItem
    success_url = reverse_lazy('notes:index')

    def post(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        model_type = request.POST.get('model_type')
        model_id = request.POST.get('model_id')
        model = apps.get_model('dishmaker', model_type)
        note = request.POST.get('note')

        instance = model.objects.get(pk=model_id)
        model_name = instance.__str__()

        context['title'] = "A note for: " + str(model_type)
        context['model_type'] = model_type
        context['model_id'] = model_id
        context['name'] = model_name
        context['description'] = instance.description

        form = NoteForm(request.POST)
        context['errors'] = form.errors

        if form.is_valid():
            content_object = instance
            noted_item = NotedItem(content_object=content_object, note=note)
            noted_item.save()
            return redirect(self.success_url)
        else:
            return self.render_to_response(context)

    def get(self, request, *args, **kwargs):
        print(request.GET)
        context = self.get_context_data(**kwargs)
        model_type = request.GET.get('model_type')
        model_id = request.GET.get('model_id')
        model = apps.get_model('dishmaker', model_type)

        instance = model.objects.get(pk=model_id)
        model_name = instance.__str__()

        context['title'] = "A note for: " + str(model_type)
        context['model_type'] = model_type
        context['model_id'] = model_id
        context['name'] = model_name
        context['description'] = instance.description

        return self.render_to_response(context)

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        return context
