from django import forms
from . import models


class ProductForm(forms.ModelForm):
    def clean_title(self):
        value = self.cleaned_data.get('title')
        if not value:
            raise forms.ValidationError('O campo é obrigatório.')
        return value

    class Meta:
        model = models.Product
        fields = ['title', 'category', 'brand', 'serie_number', 'internal_code', 'cost_price', 'selling_price', 'description']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'category': forms.Select(attrs={'class': 'form-control'}),
            'brand': forms.Select(attrs={'class': 'form-control'}),
            'serie_number': forms.TextInput(attrs={'class': 'form-control', 'required': False}),
            'cost_price': forms.NumberInput(attrs={'class': 'form-control'}),
            'selling_price': forms.NumberInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'required': False})
        }
        labels = {
            'title': 'Nome do Produto',
            'category': 'Categoria',
            'brand': 'Marca',
            'serie_number': 'Número de Série',
            'cost_price': 'Preço de Custo',
            'selling_price': 'Preço de Venda',
            'description': 'Observações'
        }
        