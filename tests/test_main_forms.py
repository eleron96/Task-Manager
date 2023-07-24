from django.contrib.auth import get_user_model
from django.test import TestCase
from task_manager.forms import UserEditForm, CreateUserForm, \
    CustomPasswordChangeForm


class TestForms(TestCase):
    def test_user_edit_form_valid_data(self):
        form = UserEditForm(data={
            'username': "testuser",
            'first_name': "test",
            'last_name': "user",
            'email': "testuser@example.com"
        })

        self.assertTrue(form.is_valid())

    def test_user_edit_form_no_data(self):
        form = UserEditForm(data={})

        self.assertFalse(form.is_valid())
        self.assertEqual(len(form.errors), 1)  # изменено с 4 на 1

    def test_create_user_form_valid_data(self):
        form = CreateUserForm(data={
            'username': "testuser",
            'first_name': "test",
            'last_name': "user",
            'password1': "strong_password_123",
            'password2': "strong_password_123",
        })

        self.assertTrue(form.is_valid())

    def test_create_user_form_no_data(self):
        form = CreateUserForm(data={})

        self.assertFalse(form.is_valid())
        self.assertEqual(len(form.errors), 5)

    def test_custom_password_change_form_valid_data(self):
        user = get_user_model().objects.create_user(
            username='testuser',
            email='testuser@example.com',
            password='testpassword'
        )

        form = CustomPasswordChangeForm(user, data={
            'old_password': "testpassword",
            'new_password1': "new_password_123",
            'new_password2': "new_password_123",
        })

        self.assertTrue(form.is_valid())

    def test_custom_password_change_form_no_data(self):
        user = get_user_model().objects.create_user(
            username='testuser',
            email='testuser@example.com',
            password='testpassword'
        )

        form = CustomPasswordChangeForm(user, data={})

        self.assertFalse(form.is_valid())
        self.assertEqual(len(form.errors), 3)
