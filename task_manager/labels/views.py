from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from task_manager.labels.models import Labels
from task_manager.labels.forms import labelsForm
from django.contrib import messages
from task_manager.tasks.models import Task, TaskLabel


@login_required
def gey_all_labels(request):
    label = Labels.objects.all()
    return render(request, 'labels/label.html', {'Labels': label})


@login_required
def create_label(request):
    if request.method == 'POST':
        form = labelsForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Метка успешно создана')
            return redirect('label')
    else:
        form = labelsForm()

    return render(request, 'labels/create_labels.html', {'form': form})
@login_required
def edit_label(request, status_id):
    status = Labels.objects.get(pk=status_id)
    if request.method == 'POST':
        # Обновляем статус
        status.name = request.POST['name']
        status.save()
        return redirect('label')

    return render(request, 'edit_labels.html', {'status': status})
@login_required
def delete_label(request, label_id):  # использовать label_id вместо status_id
    label = get_object_or_404(Labels, id=label_id)
    if request.method == 'POST':
        if not label.Tasks.exists():  # использовать label.Tasks.exists() вместо label.task_set.exists()
            label.delete()
            messages.success(request, 'Метка успешно удалена')
        else:
            messages.error(request, 'Метка не может быть удалена, так как она используется в задаче.')
        return redirect('label')

    return render(request, 'labels/confirm_delete.html', {'status': label})


@login_required
def edit_label(request, status_id):
    status = get_object_or_404(Labels, id=status_id)
    if request.method == 'POST':
        form = labelsForm(request.POST, instance=status)
        if form.is_valid():
            form.save()
            messages.success(request, "Метка успешно изменена")
            return redirect('label')
    else:
        form = labelsForm(instance=status)
    return render(request, 'labels/edit_labels.html', {'form': form})