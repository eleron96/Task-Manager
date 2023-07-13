from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import PasswordChangeForm, UserCreationForm, \
    UserChangeForm
from crispy_forms.layout import Layout, Submit
from crispy_forms.helper import FormHelper

class UserEditForm(UserChangeForm):
    first_name = forms.CharField(label='Имя', widget=forms.TextInput(attrs={'id': 'id_first_name'}))
    last_name = forms.CharField(label='Фамилия', widget=forms.TextInput(attrs={'id': 'id_last_name'}))
    username = forms.CharField(label='Имя пользователя', widget=forms.TextInput(attrs={'id': 'id_username'}))
    password1 = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'id': 'id_password1'}))
    password2 = forms.CharField(label='Подтверждение пароля', widget=forms.PasswordInput(attrs={'id': 'id_password2'}))

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username', 'password1', 'password2')

class UserPasswordChangeForm(PasswordChangeForm):
    class Meta:
        model = User

class CreateUserForm(UserCreationForm):
    first_name = forms.CharField(label='Имя')
    last_name = forms.CharField(label='Фамилия')

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username', 'password1', 'password2')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            'first_name',
            'last_name',
            'username',
            'password1',
            'password2',
            Submit('submit', 'Create', css_class='btn-primary')
        )

# class CustomPasswordChangeForm(PasswordChangeForm):
#     old_password = forms.CharField(
#         widget=forms.PasswordInput(attrs={'class': 'form-control'}))
#     new_password1 = forms.CharField(
#         widget=forms.PasswordInput(attrs={'class': 'form-control'}))
#     new_password2 = forms.CharField(
#         widget=forms.PasswordInput(attrs={'class': 'form-control'}))