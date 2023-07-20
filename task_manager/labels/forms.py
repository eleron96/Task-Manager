from django import forms
from .models import labels

class labelsForm(forms.ModelForm):
    class Meta:
        model = labels
        fields = ['name']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Введите текст', 'id': 'id_text'}),
        }
