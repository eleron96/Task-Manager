from django.contrib.auth import get_user_model
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
from task_manager.users.forms import UserEditForm, CreateUserForm
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic.edit import UpdateView

from task_manager.users.mixins import UserPermissionMixin


# Create your views here.

def user_list(request):
    users = get_user_model().objects.all()
    return render(request, 'users/users.html', {'users': users})


def create_user(request):
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Пользователь успешно зарегистрирован')
            return redirect('login')
    else:
        form = CreateUserForm()  # Используйте CreateUserForm
    return render(request, 'users/create_user.html', {'form': form})


class UserUpdateFormView(SuccessMessageMixin, LoginRequiredMixin,
                         UserPermissionMixin, UpdateView):
    """
    Update user.

    Authorization required.
    Only user can update himself.
    """

    template_name = 'users/edit_user.html'
    model = get_user_model()
    form_class = UserEditForm
    # success_url = reverse_lazy('users:user_list')
    success_message = 'Пользователь успешно изменен'
    permission_url = reverse_lazy('users:user_list')
    permission_message = 'У вас нет прав для изменения другого пользователя.'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user_form'] = self.get_form()
        return context


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
