from django.contrib.auth import login, authenticate
from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse
from requests import request
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

