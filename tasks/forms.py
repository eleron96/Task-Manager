from django import forms

from status.models import Status
from labels.models import labels
from django.contrib.auth.models import User
from .models import Task

class TaskForm(forms.ModelForm):
    name = forms.CharField(max_length=100)
    description = forms.CharField(widget=forms.Textarea)
    status = forms.ModelChoiceField(queryset=Status.objects.all())
    executor = forms.ModelChoiceField(queryset=User.objects.all())
    label = forms.ModelChoiceField(queryset=labels.objects.all(), required=False)

    class Meta:
        model = Task
        fields = ['name', 'description', 'status', 'executor', 'label']


class TaskFilterForm(forms.Form):
    status = forms.ModelChoiceField(queryset=Status.objects.all(), required=False)
    executor = forms.ModelChoiceField(queryset=User.objects.all(), required=False)
    label = forms.ModelChoiceField(queryset=labels.objects.all(), required=False)
