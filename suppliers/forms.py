from django import forms
from . import models


class SupplierForm(forms.ModelForm):

    class Meta:
        model = models.Supplier
        fields = '__all__'
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'required': False}),
            'cnpj': forms.TextInput(attrs={'class': 'form-control', 'required': False}),
            'cellphone': forms.TextInput(attrs={'class': 'form-control', 'required': False}),
            'is_whatsapp': forms.CheckboxInput(attrs={'class': 'form-check-input', 'required': False}),
            'phone': forms.TextInput(attrs={'class': 'form-control', 'required': False}),
            'cep': forms.TextInput(attrs={'class': 'form-control', 'required': False}),
            'street': forms.TextInput(attrs={'class': 'form-control', 'required': False}),
            'number': forms.TextInput(attrs={'class': 'form-control', 'required': False}),
            'neighborhood': forms.TextInput(attrs={'class': 'form-control', 'required': False}),
            'city': forms.TextInput(attrs={'class': 'form-control', 'required': False}),
            'state': forms.Select(attrs={'class': 'form-control', 'required': False}),
            'complement': forms.TextInput(attrs={'class': 'form-control', 'required': False}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'required': False}),
        }
        labels = {
            'name': 'Nome',
            'email': 'Email',
            'cnpj': 'CNPJ',
            'cellphone': 'Celular',
            'is_whatsapp': 'É WhatsApp?',
            'phone': 'Telefone',
            'cep': 'CEP',
            'street': 'Rua',
            'number': 'Número',
            'neighborhood': 'Bairro',
            'city': 'Cidade',
            'state': 'Estado',
            'complement': 'Complemento',
            'description': 'Descrição',
        }
    
    def clean(self):
        cleaned_data = super().clean()

        def limpar_numeros(valor):
            if valor:
                return ''.join(filter(str.isdigit, valor))
            return valor

        campos_a_limpar = ['cnpj', 'cep', 'phone', 'cellphone']
        for campo in campos_a_limpar:
            valor = cleaned_data.get(campo)
            cleaned_data[campo] = limpar_numeros(valor)

        return cleaned_data
