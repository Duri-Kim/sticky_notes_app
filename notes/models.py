from django.db import models


# Model representing a note
class Note(models.Model):
    title = models.CharField(max_length=200)  # Title of the note
    content = models.TextField()  # Content of the note

    def __str__(self):
        return self.title  # String representation of the Note object


# Model representing a post
class Post(models.Model):
    title = models.CharField(max_length=200)  # Title of the post
    content = models.TextField()  # Content of the post

    def __str__(self):
        return self.title  # String representation of the Post object
