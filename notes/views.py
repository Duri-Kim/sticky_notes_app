from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from .models import Note
from .forms import NoteForm


# Username of fallback guest user
GUEST_USERNAME = "guest_user"


def get_guest_user():
    """
    Retrieve or create the guest user.
    """
    guest_user, created = User.objects.get_or_create(username=GUEST_USERNAME)
    if created:
        guest_user.set_password("guest123") # Set a default password if created
        guest_user.save()
    return guest_user


# View to list all notes
def note_list(request):
    """
    Retrieve and display all notes.
    """
    notes = Note.objects.all()
    return render(request, 'notes/note_list.html', {'notes': notes})


# View to display a single note's details
def note_detail(request, pk):
    """
    Retrieve and display details of a single note.
    
    Args:
        pk (int): The primary key of the note to retrieve.
    """
    note = get_object_or_404(Note, pk=pk)
    return render(request, 'notes/note_detail.html', {'note': note})


# View to create a new note
def note_create(request):
    """
    Create a new note. Use authenticated user if available,
    otherwise fall back to guest user.
    """
    if request.method == 'POST':
        form = NoteForm(request.POST)
        if form.is_valid():
            note = form.save(commit=False)
            if request.user.is_authenticated:
                note.user = request.user 
            else:
                note.user = get_guest_user()
            note.save()
            return redirect('note_detail', pk=note.pk)
    else:
        form = NoteForm()
    return render(request, 'notes/note_form.html', {'form': form})


# View to update an existing note
def note_update(request, pk):
    """
    Handle the update of an existing note.
    
    Args:
        pk (int): The primary key of the note to update.
    """
    note = get_object_or_404(Note, pk=pk)
    if request.method == 'POST':
        form = NoteForm(request.POST, instance=note)
        if form.is_valid():
            form.save()
            return redirect('note_detail', pk=note.pk)
    else:
        form = NoteForm(instance=note)
    return render(request, 'notes/note_form.html', {'form': form})


# View to delete an existing note
def note_delete(request, pk):
    """
    Handle the deletion of an existing note.
    
    Args:
        pk (int): The primary key of the note to delete.
    """
    note = get_object_or_404(Note, pk=pk)
    note.delete()
    return redirect('note_list')
