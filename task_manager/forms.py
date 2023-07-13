from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import PasswordChangeForm, UserCreationForm
from crispy_forms.layout import Layout, Submit
from crispy_forms.helper import FormHelper


class UserEditForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username')


class CreateUserForm(UserCreationForm):
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

class UserPasswordChangeForm(PasswordChangeForm):
    new_password1 = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    new_password2 = forms.CharField(label='Подтвердите пароль', widget=forms.PasswordInput(attrs={'class': 'form-control'}))

    class Meta:
        model = User
        fields = ('new_password1', 'new_password2')
