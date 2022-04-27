from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.test import TestCase
from rest_framework import status
from django.test import Client
from ..models import Notebook, Note


class ViewNotebookTestCase(TestCase):
    def setUp(self):
        test_user = User.objects.create_user(username='TestUser', password='12345678Pas', email='test@gmail.com')
        test_user.save()

        test_notebook = Notebook.objects.create(name_notebook='TestNotebook', iduser='1')
        test_notebook.save()
        test_notebook_2 = Notebook.objects.create(name_notebook='TestNotebook_2', iduser='1')
        test_notebook_2.save()


    def test_viewes_user_notebooks(self):
        c = Client()
        user = authenticate(username='TestUser', password='12345678Pas')
        c.force_login(user)
        response = c.post('/accounts/addnotebook')
        notebook = Notebook.objects.filter(iduser=1)
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual(list(notebook.values_list('name_notebook')), [('TestNotebook',), ('TestNotebook_2',)])

    def test_create_notebook_delete_notebook(self):
        c = Client()
        user = authenticate(username='TestUser', password='12345678Pas')
        c.force_login(user)
        response = c.post('/accounts/addnotebook', {'name_notebook': 'TestNotebookCreate'})
        notebook = Notebook.objects.get(name_notebook='TestNotebookCreate')
        self.assertEqual(status.HTTP_302_FOUND, response.status_code)
        self.assertEqual(notebook.id, 3)
        self.assertEqual(notebook.name_notebook, 'TestNotebookCreate')

        response2 = c.post('/accounts/delete_notebook/3')
        notebook_delete = Notebook.objects.filter(id=3)
        self.assertEqual(list(notebook_delete), [])
        self.assertEqual(status.HTTP_302_FOUND, response2.status_code)


    def test_Notebook_name_Update(self):
        notebook = Notebook.objects.get(id=1)
        c = Client()
        user = authenticate(username='TestUser', password='12345678Pas')
        c.force_login(user)
        response = c.post('/accounts/notebook/1/update', {'name_notebook': 'TestNotebookEdit', 'iduser': '1'})
        edit_notebook = Notebook.objects.get(id=1)
        self.assertEqual(notebook.name_notebook, 'TestNotebook')
        self.assertEqual(edit_notebook.name_notebook, 'TestNotebookEdit')
        self.assertEqual(status.HTTP_302_FOUND, response.status_code)

class ViewNoteTestCase(TestCase):

    def setUp(self):
        test_user = User.objects.create_user(username='TestUser', password='12345678Pas', email='test@gmail.com')
        test_user.save()
        test_user_2 = User.objects.create_user(username='TestUser_2', password='12345678Pas_2', email='test_2@gmail.com')
        test_user_2.save()

        test_notebook = Notebook.objects.create(name_notebook='TestNotebook', iduser='1')
        test_notebook.save()
        test_notebook_2 = Notebook.objects.create(name_notebook='TestNotebook_2', iduser='2')
        test_notebook_2.save()

        test_note = Note.objects.create(title='TestTitle', text='Hallo world!!!', data='2022-04-27 15:09:40.669876+00:00', iduser='1', id_notebook='2')
        test_note.save()
        test_note_2 = Note.objects.create(title='TestTitle_2', text='Peace', data='2022-04-27 15:08:45.145466+00:00', iduser='3', id_notebook='4')
        test_note_2.save()

    def test_viewes_notebook(self):
        c = Client()
        user = authenticate(username='TestUser', password='12345678Pas')
        c.force_login(user)
        response = c.post('/accounts/notebook/2')
        response_2 = c.post('/accounts/notebook/1')
        note = Note.objects.get(iduser=1)
        self.assertEqual(status.HTTP_403_FORBIDDEN, response.status_code)
        self.assertEqual(status.HTTP_200_OK, response_2.status_code)
        self.assertEqual('TestTitle', note.title)

    def test_Note_Update(self):
        c = Client()
        user = authenticate(username='TestUser', password='12345678Pas')
        c.force_login(user)
        note = Note.objects.get(iduser=1)
        response = c.post('/accounts/view_note/2/1/update', {'title': 'TestTitleEdit', 'text': 'Hallo world!!! Edit', 'data': '2022-04-27 15:09:40.669876+00:00', 'iduser': '1', 'id_notebook': '2'})
        note_edit = Note.objects.get(iduser=1)
        self.assertEqual([note.title, note.text], ['TestTitle', 'Hallo world!!!'])
        self.assertEqual([note_edit.title, note_edit.text], ['TestTitleEdit', 'Hallo world!!! Edit'])
        self.assertEqual(status.HTTP_302_FOUND, response.status_code)

    def test_create_delete_note(self):
        c = Client()
        user = authenticate(username='TestUser', password='12345678Pas')
        c.force_login(user)
        response = c.post('/accounts/create/1', {'title': 'CreateTitle', 'text': 'Create Hallo world!!!', 'data': '2022-04-27 15:11:40.669876+00:00', 'iduser': '1', 'id_notebook': '2'})
        note_create = Note.objects.get(id=3)
        self.assertEqual([note_create.title, note_create.text], ['CreateTitle', 'Create Hallo world!!!'])
        self.assertEqual(status.HTTP_302_FOUND, response.status_code)

        response2 = c.post('/accounts/delete_note/2/3')
        note_delete = Note.objects.filter(id=3)
        self.assertEqual(status.HTTP_302_FOUND, response2.status_code)
        self.assertEqual([], list(note_delete))