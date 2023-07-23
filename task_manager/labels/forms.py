from django import forms
from .models import Labels

class labelsForm(forms.ModelForm):
    class Meta:
        model = Labels
        fields = ['name']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Введите текст', 'id': 'id_name'}),
        }