from django.test import RequestFactory, TestCase
from django.contrib.auth.models import User
from django.urls import reverse

from task_manager.views import (index, home, user_list,
                                create_user)


class ViewsTestCase(TestCase):
    def setUp(self):
        self.factory = RequestFactory()
        self.user = User.objects.create_user(
            username='testuser',
            email='testuser@example.com',
            password='testpassword'
        )
        self.client.login(username='testuser', password='testpassword')

    def test_index_view(self):
        url = reverse('index')
        request = self.factory.get(url)
        request.user = self.user
        response = index(request)
        self.assertEqual(response.status_code, 200)

    def test_home_view(self):
        url = reverse('home')
        request = self.factory.get(url)
        request.user = self.user
        response = home(request)
        self.assertEqual(response.status_code, 200)

    def test_user_list_view(self):
        url = reverse('user_list')
        request = self.factory.get(url)
        request.user = self.user
        response = user_list(request)
        self.assertEqual(response.status_code, 200)

    def test_create_user_view(self):
        url = reverse('create_user')
        request = self.factory.get(url)
        request.user = self.user
        response = create_user(request)
        self.assertEqual(response.status_code, 200)
