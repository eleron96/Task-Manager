from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404, redirect, render
from .forms import UserEditForm, CreateUserForm, \
    UserPasswordChangeForm
from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    a = None
    a.hello() # Creating an error with an invalid line of code
    return HttpResponse("Hello, world. You're at the pollapp index.")

def index(request):
    users = User.objects.all()
    return render(request, 'index.html', {'users': users})


def home(request):
    users = User.objects.all()
    return render(request, 'home.html', {'users': users})


def user_list(request):
    users = User.objects.all()
    return render(request, 'users/users.html', {'users': users})


def create_user(request):
    if request.method == 'POST':
        form = CreateUserForm(request.POST)  # Используйте CreateUserForm
        if form.is_valid():
            form.save()
            messages.success(request, 'Пользователь успешно создан.')
            return redirect('login')  # redirect to login page
    else:
        form = CreateUserForm()  # Используйте CreateUserForm
    return render(request, 'users/create_user.html', {'form': form})


@login_required
def edit_user(request, pk):
    user = User.objects.get(pk=pk)

    # Убедимся, что вошедший пользователь пытается редактировать свой профиль
    if request.user != user:
        messages.error(request, 'У вас нет прав для изменения другого '
                                'пользователя.', extra_tags='danger')
        return redirect('user_list')

    if request.method == 'POST':
        user_form = UserEditForm(request.POST, instance=user)
        password_form = UserPasswordChangeForm(user, request.POST)

        if user_form.is_valid():
            user_form.save()
            messages.success(request, 'Ваш профиль успешно обновлен!')

            # Проверяем, заполнены ли поля пароля
            if password_form.has_changed() and password_form.is_valid():
                password_form.save()
                messages.success(request,
                                 'Ваш профиль успешно обновлен!')

            return redirect('user_list')
    else:
        user_form = UserEditForm(instance=user)
        password_form = UserPasswordChangeForm(user)

    context = {
        'user_form': user_form,
        'password_form': password_form,
    }

    return render(request, 'users/edit_user.html', context)


def login_view(request):
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
                                 'могут быть чувствительны к регистру.', extra_tags='danger')
        else:
            for msg in form.non_field_errors():
                messages.error(request, msg)
    else:
        form = AuthenticationForm()
        if 'next' in request.GET:
            messages.error(request, 'Пожалуйста, войдите, чтобы продолжить.', extra_tags='danger')
    return render(request, 'registration/login.html', {'form': form})



def logout_view(request):
    logout(request)
    messages.info(request, 'Вы разлогинены')
    return redirect('home')


@login_required
def delete_user(request, id):
    user = User.objects.get(id=id)
    if request.user != user:
        messages.error(request, 'У вас нет прав для изменения другого '
                                'пользователя.')
        return redirect('user_list')
    if request.method == 'POST':
        user.delete()
        messages.success(request, 'Пользователь успешно удален.')
        return redirect('user_list')
    else:
        return render(request, 'users/confirm_delete.html', {'user': user})
