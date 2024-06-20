from django.test import TestCase
from django.urls import reverse
from .models import Note, Post


# Test case for Note model
class NoteModelTest(TestCase):

    def setUp(self):
        # Create a Note object for testing
        Note.objects.create(title='Test Note', content='This is a test note.')

    def test_note_has_title(self):
        # Test that the note has the expected title
        note = Note.objects.get(id=1)
        self.assertEqual(note.title, 'Test Note')

    def test_note_has_content(self):
        # Test that the note has the expected content
        note = Note.objects.get(id=1)
        self.assertEqual(note.content, 'This is a test note.')


# Test case for Note views
class NoteViewTest(TestCase):

    def setUp(self):
        # Create a Note object for testing
        Note.objects.create(title='Test Note', content='This is a test note.')

    def test_note_list_view(self):
        # Test the note list view
        response = self.client.get(reverse('note_list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Test Note')

    def test_note_detail_view(self):
        # Test the note detail view
        note = Note.objects.get(id=1)
        response = self.client.get(reverse('note_detail', args=[str(note.id)]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Test Note')
        self.assertContains(response, 'This is a test note.')


# Test case for Post model
class PostModelTest(TestCase):

    def setUp(self):
        # Create a Post object for testing
        Post.objects.create(title='Test Post', content='This is a test post.')

    def test_post_has_title(self):
        # Test that the post has the expected title
        post = Post.objects.get(id=1)
        self.assertEqual(post.title, 'Test Post')

    def test_post_has_content(self):
        # Test that the post has the expected content
        post = Post.objects.get(id=1)
        self.assertEqual(post.content, 'This is a test post.')


# Test case for Post views
class PostViewTest(TestCase):

    def setUp(self):
        # Create a Post object for testing
        Post.objects.create(title='Test Post', content='This is a test post.')

    def test_post_list_view(self):
        # Test the post list view
        response = self.client.get(reverse('post_list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Test Post')

    def test_post_detail_view(self):
        # Test the post detail view
        post = Post.objects.get(id=1)
        response = self.client.get(reverse('post_detail', args=[str(post.id)]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Test Post')
        self.assertContains(response, 'This is a test post.')
