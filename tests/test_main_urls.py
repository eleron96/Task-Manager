from unittest import TestCase

from django.urls import reverse, resolve
from task_manager import views


class TestUrls(TestCase):

    def test_index_url(self):
        path = reverse('index')
        self.assertEqual(resolve(path).func, views.index)

    def test_home_url(self):
        path = reverse('home')
        self.assertEqual(resolve(path).func, views.home)

    def test_login_url(self):
        path = reverse('login')
        self.assertEqual(resolve(path).func, views.login_view)

    def test_logout_url(self):
        path = reverse('logout')
        self.assertEqual(resolve(path).func, views.logout_view)

    def test_user_list_url(self):
        path = reverse('user_list')
        self.assertEqual(resolve(path).func, views.user_list)

    def test_create_user_url(self):
        path = reverse('create_user')
        self.assertEqual(resolve(path).func, views.create_user)
