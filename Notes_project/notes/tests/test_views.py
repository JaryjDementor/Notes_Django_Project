from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse
from rest_framework import status

from django.test import Client

from ..models import Notebook


class ViewNotebookTestCase(TestCase):
    def setUp(self):
        test_user = User.objects.create(username='TestUser', password='12345678Pas', email='test@gmail.com')
        test_user.save()
        c = Client()
        a = c.login(username='TestUser', password='12345678Pas')

        # test_user_login = User.objects.login(username='TestUser', password='12345678Pas')
        # test_user_login.save()

    # def setUpTestData(self):
    #     test_user = Notebook.objects.login(name_notebook='TestNotebook', iduser='2')
    #     test_user.save()

    def test_register_request_uncorrect_request(self):
        c = Client()
        # a=c.login(username='TestUser', password='12345678Pas')
        url = reverse('add_notebook')
        # response = c.post(url, {'name_notebook': 'TestNotebook1', 'iduser': '2'})
        response = c.post('/accounts/addnotebook', {'name_notebook': 'TestNotebook1'})
        print(response.status_code)
        # self.assertEqual(status.HTTP_400_BAD_REQUEST, response.status_code)

