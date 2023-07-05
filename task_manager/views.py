from django.contrib import messages
from django.contrib.auth import authenticate, get_user_model, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404, redirect, render
from .forms import CustomPasswordChangeForm, UserEditForm


def index(request):
    users = User.objects.all()
    return render(request, 'index.html', {'users': users})


def home(request):
    users = User.objects.all()
    return render(request, 'home.html', {'users': users})


def user_detail(request, id):
    user = get_object_or_404(User, pk=id)
    return render(request, 'user_detail.html', {'user': user})


def user_list(request):
    users = User.objects.all()
    return render(request, 'users/users.html', {'users': users})


def create_user(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('user_list')
    else:
        form = UserCreationForm()
    return render(request, 'users/create_user.html', {'form': form})


@login_required
def edit_user(request, id):
    User = get_user_model()
    user = User.objects.get(id=id)

    # Ensure the logged in user is the one trying to edit their profile
    if request.user != user:
        messages.error(request, 'You are not allowed to edit this user.')
        return redirect('home')

    if request.method == 'POST':
        u_form = UserEditForm(request.POST, instance=user)
        p_form = CustomPasswordChangeForm(user, request.POST)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, 'Your profile was successfully updated!')
            return redirect('home')
    else:
        u_form = UserEditForm(instance=user)
        p_form = CustomPasswordChangeForm(user)

    return render(request, 'users/edit_user.html',
                  {'u_form': u_form, 'p_form': p_form})


def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
    else:
        form = AuthenticationForm()
    return render(request, 'registration/login.html', {'form': form})

def delete_user(request, id):
    user = get_object_or_404(User, id=id)
    if request.method == 'POST':
        user.delete()
        return redirect('task_manager:user_list')
    return render(request, 'confirm_delete.html', {'object': user})
