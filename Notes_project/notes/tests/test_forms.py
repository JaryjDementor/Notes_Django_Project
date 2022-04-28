from django.test import TestCase
from ..forms import NotebookForm, NoteUserForm


class NotebookFormTestCase(TestCase):
    def test_NewUserForm_False(self):
        form_data = {'name_notebook': ''}
        form = NotebookForm(data=form_data)
        self.assertFalse(form.is_valid())

    def test_NewUserForm_True(self):
        form_data = {'name_notebook': 'Test1'}
        form = NotebookForm(data=form_data)
        self.assertTrue(form.is_valid())


class NoteUserFormTestCase(TestCase):
    def test_NoteUserForm_False(self):
        form_data = {'title': '', 'text': ''}
        form = NoteUserForm(data=form_data)
        self.assertFalse(form.is_valid())

    def test_NoteUserForm_True(self):
        form_data = {'title': 'Test1', 'text': 'Hallo world!'}
        form = NoteUserForm(data=form_data)
        self.assertTrue(form.is_valid())

