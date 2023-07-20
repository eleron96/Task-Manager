from django import forms

from django.contrib.auth.forms import PasswordChangeForm, UserCreationForm
from crispy_forms.layout import Layout, Submit
from crispy_forms.helper import FormHelper
from django.contrib.auth import password_validation, get_user_model


class UserEditForm(UserCreationForm):
    class Meta:
        model = get_user_model()
        fields = ('first_name', 'last_name', 'username')


class CreateUserForm(UserCreationForm):
    class Meta:
        model = get_user_model()
        fields = (
        'first_name', 'last_name', 'username', 'password1', 'password2')

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
    new_password1 = forms.CharField(label='Пароль', widget=forms.PasswordInput(
        attrs={'class': 'form-control'}))
    new_password2 = forms.CharField(label='Подтвердите пароль',
                                    widget=forms.PasswordInput(
                                        attrs={'class': 'form-control'}))

    class Meta:
        model = get_user_model()
        fields = ('new_password1', 'new_password2')


class UserEditForm(forms.ModelForm):
    new_password1 = forms.CharField(label='Новый пароль',
                                    widget=forms.PasswordInput(
                                        attrs={'class': 'form-control'}),
                                    required=False)
    new_password2 = forms.CharField(label='Подтверждение нового пароля',
                                    widget=forms.PasswordInput(
                                        attrs={'class': 'form-control'}),
                                    required=False)

    class Meta:
        model = get_user_model()
        fields = (
        'first_name', 'last_name', 'username', 'new_password1', 'new_password2')

    def clean_username(self):
        username = self.cleaned_data.get('username')
        if get_user_model().objects.filter(username=username).exclude(
                pk=self.instance.pk).exists():
            raise forms.ValidationError(
                'Пользователь с таким именем уже существует.')
        return username

    def clean(self):
        cleaned_data = super().clean()
        password1 = cleaned_data.get("new_password1")
        password2 = cleaned_data.get("new_password2")
        if password1 or password2:
            if password1 != password2:
                self.add_error('new_password2', "Пароли не совпадают")
            else:
                password_validation.validate_password(password2, self.instance)
        return cleaned_data

    def save(self, commit=True):
        user = super().save(commit=False)
        password = self.cleaned_data.get("new_password1")
        if password:
            user.set_password(password)
        if commit:
            user.save()
        return user
