from django import forms
from . import models


class InflowForm(forms.ModelForm):
    
    class Meta:
        model = models.Inflow
        fields = ['supplier', 'product', 'purchase_price', 'invoice_number', 'quantity', 'description']
        widgets = {
            'supplier': forms.Select(attrs={'class': 'form-control'}),
            'product': forms.Select(attrs={'class': 'form-control'}),
            'purchase_price': forms.NumberInput(attrs={'class': 'form-control', 'required': False}),
            'invoice_number': forms.NumberInput(attrs={'class': 'form-control', 'required': False}),
            'quantity': forms.NumberInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'required': False})
        }
        labels = {
            'supplier': 'Fornecedor',
            'product': 'Produto',
            'purchase_price': 'Preço de Compra',
            'invoice_number': 'Número da Nota Fiscal',
            'quantity': 'Quantidade',
            'description': 'Observações'
        }
