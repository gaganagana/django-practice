from django.test import TestCase, Client
from django.urls import reverse
from .models import Note, Category
from .forms import NoteForm


class NoteModelTestCase(TestCase):
    def setUp(self):
        self.category = Category.objects.create(name='Tutorials', slug='tutorials')
        self.note = Note.objects.create(
            title='Learn Django ORM',
            content='Django ORM provides high-level Python database abstraction.',
            category=self.category,
            priority=Note.PRIORITY_HIGH,
        )

    def test_note_creation(self):
        self.assertEqual(self.note.title, 'Learn Django ORM')
        self.assertEqual(self.note.priority, 'high')
        self.assertFalse(self.note.is_archived)

    def test_string_representation(self):
        self.assertEqual(str(self.note), 'Learn Django ORM (High Priority)')

    def test_word_count(self):
        self.assertGreater(self.note.word_count, 5)


class NoteFormTestCase(TestCase):
    def test_valid_form(self):
        form = NoteForm(data={
            'title': 'Build a REST API',
            'content': 'Using Django REST framework to build clean endpoints.',
            'priority': 'medium',
            'is_archived': False,
        })
        self.assertTrue(form.is_valid())

    def test_short_title_invalid(self):
        form = NoteForm(data={
            'title': 'Hi',
            'content': 'Short title test',
            'priority': 'low',
        })
        self.assertFalse(form.is_valid())
        self.assertIn('title', form.errors)


class NoteViewTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        self.note = Note.objects.create(title='Sample View Test', content='Testing view status codes.')

    def test_note_list_status_200(self):
        response = self.client.get(reverse('notes:list'))
        self.assertEqual(response.status_code, 200)

    def test_note_detail_status_200(self):
        response = self.client.get(reverse('notes:detail', kwargs={'pk': self.note.pk}))
        self.assertEqual(response.status_code, 200)
