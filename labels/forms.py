from django import forms
from .models import labels

class labelsForm(forms.ModelForm):
    class Meta:
        model = labels
        fields = ['name']
