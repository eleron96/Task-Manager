from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from labels.models import labels
from labels.forms import labelsForm
from django.contrib import messages

@login_required
def label(request):
    label = labels.objects.all()
    return render(request, 'labels/label.html', {'labels': label})


@login_required
def create_label(request):
    if request.method == 'POST':
        form = labelsForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Метка успешно создана!')
            return redirect('label')
    else:
        form = labelsForm()

    return render(request, 'labels/create_labels.html', {'form': form})
@login_required
def edit_label(request, status_id):
    status = labels.objects.get(pk=status_id)
    if request.method == 'POST':
        # Обновляем статус
        status.name = request.POST['name']
        status.save()
        return redirect('label')

    return render(request, 'edit_labels.html', {'status': status})
@login_required
def delete_label(request, status_id):
    status = labels.objects.get(pk=status_id)
    if request.method == 'POST':
        status.delete()
        return redirect('label')

    return render(request, 'labels/confirm_delete.html', {'status': status})

@login_required
def edit_label(request, status_id):
    status = get_object_or_404(labels, id=status_id)
    if request.method == 'POST':
        form = labelsForm(request.POST, instance=status)
        if form.is_valid():
            form.save()
            messages.success(request, "Метка успешно обновлен!")
            return redirect('label')
    else:
        form = labelsForm(instance=status)
    return render(request, 'labels/edit_labels.html', {'form': form})