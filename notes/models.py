from django.db import models
from django.contrib.auth.models import User


class Note(models.Model):
    """
    Model representing a note.

    Attributes:
        title (str): The title of the note, with a maximum length of 200
        characters.
        content (str): The content of the note.
        user (User): The user associated with the note. This is a foreign key
        to the User model.
    """
    title = models.CharField(max_length=200)
    content = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        """
        String representation of the Note object, returning the title.
        """
        return self.title


class Post(models.Model):
    """
    Model representing a post.

    Attributes:
        title (str): The title of the post, with a maximum length of 200
        characters.
        content (str): The content of the post.
        user (User): The user associated with the post. This is a foreign key
        to the User model.
    """
    title = models.CharField(max_length=200)
    content = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        """
        String representation of the Post object, returning the title.
        """
