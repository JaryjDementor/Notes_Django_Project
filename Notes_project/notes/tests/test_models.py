from datetime import datetime
from django.test import TestCase
from ..models import Notebook, Note


class NotebookTestCase(TestCase):
    @classmethod
    def setUpTestData(cls):
        notebook = Notebook.objects.create(name_notebook="Test1", iduser="2")

    def test_name_notebook_label(self):
        notebook = Notebook.objects.get(id=1)
        field_label = notebook._meta.get_field("name_notebook").verbose_name
        self.assertEquals(field_label, "name_notebook")

    def test_name_iduser_label(self):
        notebook = Notebook.objects.get(id=1)
        field_label = notebook._meta.get_field("iduser").verbose_name
        self.assertEquals(field_label, "iduser")

    def test_get_absolute_url(self):
        notebook = Notebook.objects.get(id=1)
        self.assertEquals(notebook.get_absolute_url(), "/accounts/notebook/1")


class NoteTestCase(TestCase):
    @classmethod
    def setUpTestData(cls):
        notebook = Note.objects.create(
            title="Test1",
            text="Hallo world!!!",
            data=datetime.now(),
            iduser="2",
            id_notebook="3",
        )

    def test_name_title_label(self):
        note = Note.objects.get(id=1)
        field_label = note._meta.get_field("title").verbose_name
        self.assertEquals(field_label, "title")

    def test_name_text_label(self):
        note = Note.objects.get(id=1)
        field_label = note._meta.get_field("text").verbose_name
        self.assertEquals(field_label, "text")

    def test_name_data_label(self):
        note = Note.objects.get(id=1)
        field_label = note._meta.get_field("data").verbose_name
        self.assertEquals(field_label, "data")

    def test_name_iduser_label(self):
        note = Note.objects.get(id=1)
        field_label = note._meta.get_field("iduser").verbose_name
        self.assertEquals(field_label, "iduser")

    def test_name_id_notebook_label(self):
        note = Note.objects.get(id=1)
        field_label = note._meta.get_field("id_notebook").verbose_name
        self.assertEquals(field_label, "id_notebook")

    def test_get_absolute_url(self):
        notebook = Note.objects.get(id=1)
        self.assertEquals(notebook.get_absolute_url(), "/accounts/view_note/3/1")
