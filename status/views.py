from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from status.models import Status
from status.forms import StatusForm
from django.contrib import messages
from tasks.models import Task

@login_required
def status_task(request):
    statuses = Status.objects.all()
    return render(request, 'status/status_task.html', {'statuses': statuses})


@login_required
def create_status(request):
    if request.method == 'POST':
        form = StatusForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Статус успешно создан!')
            return redirect('status_task')
    else:
        form = StatusForm()

    return render(request, 'status/create_status.html', {'form': form})
@login_required
def edit_status(request, status_id):
    status = Status.objects.get(pk=status_id)
    if request.method == 'POST':
        # Обновляем статус
        status.name = request.POST['name']
        status.save()
        return redirect('status_task')

    return render(request, 'edit_status.html', {'status': status})
@login_required
def delete_status(request, status_id):
    status = get_object_or_404(Status, id=status_id)
    if request.method == 'POST':
        if not Task.objects.filter(status=status).exists(): # Проверяем, используется ли статус в задачах
            status.delete()
            messages.success(request, 'Статус успешно удалён!')
        else:
            messages.error(request, 'Статус не может быть удалён, так как он используется в задаче.')
        return redirect('status_task')

    return render(request, 'status/confirm_delete.html', {'status': status})

@login_required
def edit_status(request, status_id):
    status = get_object_or_404(Status, id=status_id)
    if request.method == 'POST':
        form = StatusForm(request.POST, instance=status)
        if form.is_valid():
            form.save()
            messages.success(request, "Статус успешно обновлен!")
            return redirect('status_task')  # Or wherever you want to redirect after successful form submission
    else:
        form = StatusForm(instance=status)
    return render(request, 'status/edit_status.html', {'form': form})