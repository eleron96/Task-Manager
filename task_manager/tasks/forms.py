from django import forms
from django.contrib.auth import get_user_model

from task_manager.status.models import Status
from task_manager.labels.models import labels
from .models import Task


class TaskForm(forms.ModelForm):
    name = forms.CharField(max_length=100)
    description = forms.CharField(widget=forms.Textarea)
    status = forms.ModelChoiceField(queryset=Status.objects.all())
    executor = forms.ModelChoiceField(queryset=get_user_model().objects.all())
    label = forms.ModelChoiceField(queryset=labels.objects.all(), required=False)

    class Meta:
        model = Task
        fields = ['name', 'description', 'status', 'executor', 'label']

    def clean_status(self):
        status = self.cleaned_data.get('status')
        if status:
            return Status.objects.get(id=status.id)  # or status.id if status is an instance
        return status


class TaskFilterForm(forms.Form):
    status = forms.ModelChoiceField(queryset=Status.objects.all(), required=False)
    executor = forms.ModelChoiceField(queryset=get_user_model().objects.all(), required=False)
    label = forms.ModelChoiceField(queryset=labels.objects.all(), required=False)
    my_tasks = forms.BooleanField(required=False)

