from django.contrib.auth.models import User
from django.test import TestCase
from rest_framework import status

from django.test import Client


class ViewTestCase(TestCase):
    def setUp(self):
        test_user = User.objects.create_user(username='TestUser', password='12345678Pas', email='test@gmail.com')
        test_user.save()


    def test_first_page(self):
        c = Client()
        response = c.get('')
        self.assertEqual(status.HTTP_200_OK, response.status_code)

    def test_register_request_uncorrect_request(self):
        c = Client()
        response = c.post('/register', {'username': 'TestUser', 'email': 'example', 'password': '12345678Pas', 'password2': ''})
        self.assertEqual(status.HTTP_400_BAD_REQUEST, response.status_code)

    def test_register_request_current_email(self):
        c = Client()
        response = c.post('/register', {'username': 'TestUser', 'email': 'test@gmail.com', 'password': '12345678Pas', 'password2': '12345678Pas'})
        self.assertEqual(status.HTTP_400_BAD_REQUEST, response.status_code)

    def test_register_request_correct_request(self):
        c = Client()
        response = c.post('/register', {'username': 'TestUser1', 'email': 'test1@gmail.com', 'password1': '12345678Pas', 'password2': '12345678Pas'})
        self.assertEqual(status.HTTP_302_FOUND, response.status_code)

    def test_login_request_uncorrect_request(self):
        c = Client()
        response = c.post('/login', {'username': 'TestUser', 'password': '12345678'})
        self.assertEqual(status.HTTP_400_BAD_REQUEST, response.status_code)

    def test_login_request_correct_request(self):
        c = Client()
        response = c.post('/login', {'username': 'TestUser', 'password': '12345678Pas'})
        self.assertEqual(status.HTTP_302_FOUND, response.status_code)

    def test_logout_request(self):
        c = Client()
        response = c.get('/logout')
        self.assertEqual(status.HTTP_302_FOUND, response.status_code)


































# # from django.conf import settings
# from django.contrib.auth.models import User
# from django.test import TestCase
# # from .logic import num
# from django.test import Client
# # Create your tests here.
#
# # settings.configure()
# from django.urls import reverse
# from rest_framework import status
#
#
# class ViewTestCase(TestCase):
#     def setUp(self):
#         # test_user1 = User.objects.create_user(username='testuser1', email='testuser1@gmail.com', password='12345678Pas')
#         test_user1.save()
#     # def test_login_request(self):
#     #     a=self.client.login(username='testuser1', password='12345678Pas')
#     #     resp = self.client.get(reverse('view notebooks'))
#     #     self.assertEqual(str(resp.context['user']), 'testuser1')
#     #     # self.assertEqual(status.HTTP_200_OK,resp )
#     #     self.assertEqual(resp.status_code, 200)
#     def test_register_request(self):
#         # c = Client()
#
#         response = c.post('register', {'username': 'TestUser', 'email': 'testuser@gmail.com', 'password1': '123456Pas', 'password2': '123456Pas'})
#         self.assertEqual(status.HTTP_302_FOUND,response.status_code)
#
#
#
#
#
#
#
# # class LogicTestCase(TestCase):
# #     def test_num_plus(self):
# #         a=num(7,2,'+')
# #         self.assertEqual(9,a)
# #     def test_num_minus(self):
# #         a=num(7,2,'-')
# #         self.assertEqual(5,a)
#
#