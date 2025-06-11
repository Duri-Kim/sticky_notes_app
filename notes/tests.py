from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from .models import Note, Post


class NoteModelTest(TestCase):
    """Test case for Note model."""

    def setUp(self):
        """Set up a Note object for testing."""
        self.user = User.objects.create_user(
            username='testuser', password='testpass'
        )
        Note.objects.create(
            title='Test Note', content='This is a test note.', user=self.user
        )

    def test_note_has_title(self):
        """Test that the note has the expected title."""
        note = Note.objects.get(id=1)
        self.assertEqual(note.title, 'Test Note')

    def test_note_has_content(self):
        """Test that the note has the expected content."""
        note = Note.objects.get(id=1)
        self.assertEqual(note.content, 'This is a test note.')


class NoteViewTest(TestCase):
    """Test case for Note views."""

    def setUp(self):
        """Set up a Note object for testing."""
        self.user = User.objects.create_user(
            username='testuser', password='testpass'
        )
        self.note = Note.objects.create(
            title='Test Note', content='This is a test note.', user=self.user
        )

    def test_note_list_view(self):
        """Test the note list view."""
        response = self.client.get(reverse('note_list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Test Note')

    def test_note_detail_view(self):
        """Test the note detail view."""
        response = self.client.get(reverse('note_detail', args=[str(
            self.note.id)])
        )
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Test Note')
        self.assertContains(response, 'This is a test note.')
