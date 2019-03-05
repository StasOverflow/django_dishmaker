from django.shortcuts import render
from django.views.generic.list import ListView
from .models import Note


class NoteListView(ListView):
    model = Note
    title = 'Note list'
    template_name = 'notes/note_list.html'

    def get_context_data(self, **kwargs):
        context = super(NoteListView, self).get_context_data()
        context['title'] = self.title
        return context
