from django import forms
from . import models


class BrandForm(forms.ModelForm):
    
    class Meta:
        model = models.Brand
        fields = ['name', 'website', 'description']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'website': forms.TextInput(attrs={'class': 'form-control', 'required': False}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'required': False})
        }
        labels = {
            'name': 'Nome',
            'website': 'Website',
            'description': 'Descrição'
        }