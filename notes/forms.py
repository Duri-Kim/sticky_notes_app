from django import forms
from .models import Note


# Form for creating and updating notes
class NoteForm(forms.ModelForm):
    class Meta:
        model = Note
        fields = ['title', 'content']  # Fields to be included in the form
