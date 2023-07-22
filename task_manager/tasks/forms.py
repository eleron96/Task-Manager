from django import forms
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _

from task_manager.status.models import Status
from task_manager.labels.models import labels
from .models import Task
from ..users.models import User


class TaskForm(forms.ModelForm):
    name = forms.CharField(max_length=100, label=_('Name'))
    description = forms.CharField(widget=forms.Textarea, label=_('Description'))
    status = forms.ModelChoiceField(queryset=Status.objects.all(), label=_('Status'))
    # executor = forms.ModelChoiceField(queryset=get_user_model().objects.all(), label=_('Executor'))
    executor = forms.ModelChoiceField(queryset=User.objects.all(), label=_('Executor'))
    label = forms.ModelChoiceField(queryset=labels.objects.all(), required=False, label=_('Labels'))


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
    executor = forms.ModelChoiceField(queryset=User.objects.all(), required=False)
    label = forms.ModelChoiceField(queryset=labels.objects.all(), required=False)
    my_tasks = forms.BooleanField(required=False)

