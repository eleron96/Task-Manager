from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required

from task_manager.status.models import Status
from task_manager.tasks.models import Task as TaskModel
from task_manager.tasks.forms import TaskForm, TaskFilterForm
from django.contrib import messages


# @login_required
# def create_tasks(request):
#     if request.method == 'POST':
#         form = TaskForm(request.POST)
#         if form.is_valid():
#             task = form.save(
#                 commit=True)  # Save the form, but don't commit to the database yet
#             task.author = request.user  # Set the author to the currently logged-in user
#             task.status = form.cleaned_data['status']
#             task.executor = form.cleaned_data['executor']
#             task.label = form.cleaned_data['label']
#             task.save()  # Now commit to the database
#             messages.success(request, 'Задача успешно создана!')
#             return redirect('tasks')
#     else:
#         form = TaskForm()
#     return render(request, 'tasks/create_tasks.html', {'form': form})

@login_required
def create_tasks(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            # Мы непосредственно сохраняем форму, прежде чем сделать какие-либо изменения
            task = form.save(commit=False)
            task.author = request.user  # Задаем автора как текущего пользователя
            task.save()  # Сохраняем изменения
            messages.success(request, 'Задача успешно создана!')
            return redirect('tasks')
    else:
        form = TaskForm()
    return render(request, 'tasks/create_tasks.html', {'form': form})


@login_required
def task(request, task_id):
    task = TaskModel.objects.get(pk=task_id)
    if request.method == 'POST':
        # Обновляем статус
        task.name = request.POST['name']
        task.save()
        return redirect('tasks')

    return render(request, 'edit_task.html', {'task': task})


@login_required
def delete_tasks(request, task_id):
    task = get_object_or_404(TaskModel, pk=task_id)

    # Check if the logged-in user is the author of the task
    if task.author != request.user:
        messages.error(request, "У вас нет прав для редактирования этой задачи")
        return redirect('tasks')

    if request.method == 'POST':
        task.delete()
        messages.success(request, "Задача успешно обновлена")
        return redirect('tasks')

    return render(request, 'tasks/confirm_delete.html', {'task': task})


@login_required
def edit_tasks(request, task_id):
    task = get_object_or_404(TaskModel, id=task_id)

    # Check if the logged-in user is the author of the task
    if task.author != request.user:
        messages.error(request, "У вас нет прав для редактирования этой задачи")
        return redirect('tasks')

    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            messages.success(request, "Задача успешно обновлена")
            return redirect('tasks')
    else:
        form = TaskForm(instance=task)

    return render(request, 'tasks/edit_tasks.html',
                  {'form': form, 'task': task})


@login_required
def tasks_list(request):
    form = TaskFilterForm(request.GET or None)
    tasks = TaskModel.objects.all()
    statuses = Status.objects.all()
    if form.is_valid():
        if form.cleaned_data['status']:
            tasks = tasks.filter(status=form.cleaned_data['status'].id)
        if form.cleaned_data['executor']:
            tasks = tasks.filter(executor=form.cleaned_data['executor'].id)
        if form.cleaned_data['label']:
            tasks = tasks.filter(label=form.cleaned_data['label'].id)
        if form.cleaned_data['my_tasks']:  # Check if 'my_tasks' is checked
            tasks = tasks.filter(
                author=request.user)
    context = {'form': form, 'tasks': tasks,
               'task_statuses': statuses}
    return render(request, 'tasks/tasks.html', context)
