from django.contrib import messages
from django.contrib.auth import authenticate, login, logout, get_user_model
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import redirect, render
from task_manager.users.forms import UserEditForm
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic.edit import UpdateView


def index(request):
    users = get_user_model().objects.all()
    return render(request, 'index.html', {'users': users})


def home(request):
    users = get_user_model().objects.all()
    return render(request, 'home.html', {'users': users})


def login_view(request):  # noqa: C901
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, 'Вы залогинены',
                                 extra_tags='success')
                if 'next' in request.POST:
                    return redirect(request.POST.get('next'))
                else:
                    return redirect('home')
            else:
                messages.error(request, 'Пожалуйста, введите правильные имя '
                                        'пользователя и пароль. Оба поля '
                                        'могут быть чувствительны к регистру.',
                               extra_tags='danger')
        else:
            for msg in form.non_field_errors():
                messages.error(request, msg)
    else:
        form = AuthenticationForm()
        if 'next' in request.GET:
            messages.error(request, 'Пожалуйста, войдите, чтобы продолжить.',
                           extra_tags='danger')
    return render(request, 'registration/login.html', {'form': form})


def logout_view(request):
    logout(request)
    messages.info(request, 'Вы разлогинены')
    return redirect('home')


@login_required
def delete_user(request, pk):
    user = get_user_model().objects.get(pk=pk)
    if request.user != user:
        messages.error(request, 'У вас нет прав для изменения другого '
                                'пользователя.')
        return redirect('users:user_list')
    if request.method == 'POST':
        user.delete()
        messages.success(request, 'Пользователь успешно удален.')
        return redirect('users:user_list')
    else:
        return render(request, 'users/confirm_delete.html', {'user': user})


class UserEditView(UpdateView, SuccessMessageMixin):
    model = get_user_model()
    template_name = 'users/edit_user.html'
    form_class = UserEditForm
    success_url = '/users/'
    success_message = 'Пользователь успешно изменен'
