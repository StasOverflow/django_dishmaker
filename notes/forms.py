from django import forms


class NoteForm(forms.Form):
    note = forms.CharField(label='Your name', max_length=100, min_length=4)
