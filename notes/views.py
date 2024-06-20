from django.shortcuts import render, redirect, get_object_or_404
from .models import Note, Post
from .forms import NoteForm, PostForm


# View to list all notes
def note_list(request):
    # Retrieve all notes from the database
    notes = Note.objects.all()  
    # Render the note list template with the notes
    return render(request, 'notes/note_list.html', {'notes': notes})


# View to display a single note's details
def note_detail(request, pk):
    # Retrieve the note by primary key or return a 404 error if not found
    note = get_object_or_404(Note, pk=pk)
    # Render the note detail template with the note
    return render(request, 'notes/note_detail.html', {'note': note})


# View to create a new note
def note_create(request):
    if request.method == 'POST':
        # Bind data from the request to the form
        form = NoteForm(request.POST)  
        if form.is_valid():
            # Save the new note to the database
            form.save()
            # Redirect to the note list view
            return redirect('note_list')  
    else:
        # Create an empty form
        form = NoteForm()
    # Render the note form template  
    return render(request, 'notes/note_form.html', {'form': form})


# View to update an existing note
def note_update(request, pk):
    # Retrieve the note by primary key or return a 404 error if not found
    note = get_object_or_404(Note, pk=pk)
    if request.method == 'POST':
        # Bind data from the request to the form
        # with the existing note instance
        form = NoteForm(request.POST, instance=note)
        if form.is_valid():
            # Save the updated note to the database
            form.save()
            # Redirect to the note detail view
            return redirect('note_detail', pk=note.pk)
    else:
        # Create a form pre-populated with the existing note's data
        form = NoteForm(instance=note)
    # Render the note form template
    return render(request, 'notes/note_form.html', {'form': form})


# View to delete an existing note
def note_delete(request, pk):
    # Retrieve the note by primary key or return a 404 error if not found
    note = get_object_or_404(Note, pk=pk)
    # Delete the note from the database
    note.delete()
    # Redirect to the note list view
    return redirect('note_list')


# View to list all posts
def post_list(request):
    # Retrieve all posts from the database
    posts = Post.objects.all()
    # Render the post list template with the posts
    return render(request, 'notes/post_list.html', {'posts': posts})


# View to display a single post's details
def post_detail(request, pk):
    # Retrieve the post by primary key or return a 404 error if not found
    post = get_object_or_404(Post, pk=pk)
    # Render the post detail template with the post
    return render(request, 'notes/post_detail.html', {'post': post})


# View to create a new post
def post_create(request):
    if request.method == 'POST':
        # Bind data from the request to the form
        form = PostForm(request.POST)
        if form.is_valid():
            # Save the new post to the database
            post = form.save()
            # Redirect to the post list view
            return redirect('post_detail', pk=post.pk)
    else:
        # Create an empty form
        form = PostForm()
    # Render the post form template
    return render(request, 'notes/post_form.html', {'form': form})


# View to update an existing post
def post_update(request, pk):
    # Retrieve the post by primary key or return a 404 error if not found
    post = get_object_or_404(Post, pk=pk)
    if request.method == 'POST':
        form = PostForm(request.POST, instance=post)
        # Bind data from the request to the form
        # with the existing post instance
        if form.is_valid():
            # Save the updated post to the database
            form.save()
            # Redirect to the post detail view
            return redirect('post_detail', pk=post.pk)
    else:
        # Create a form pre-populated with the existing post's data
        form = PostForm(instance=post)
    # Render the post form template
    return render(request, 'notes/post_form.html', {'form': form})


# View to delete an existing post
def post_delete(request, pk):
    # Retrieve the post by primary key or return a 404 error if not found
    post = get_object_or_404(Post, pk=pk)
    # Delete the post from the database
    post.delete()
    # Redirect to the post list view
    return redirect('post_list')
