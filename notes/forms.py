from django import forms
from .models import Note, Post


# Form for creating and updating notes
class NoteForm(forms.ModelForm):
    class Meta:
        model = Note
        fields = ['title', 'content']  # Fields to be included in the form


# Form for creating and updating posts
class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        # Fields to be included in the form
        fields = ['title', 'content']
