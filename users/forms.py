# forms.py
from django import forms
from django.contrib.auth.models import User
from .models import Profile


class UserForm(forms.ModelForm):
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control'}),
        label='Senha'
    )
    role = forms.ChoiceField(
        choices=Profile.ROLE_CHOICES,
        widget=forms.Select(attrs={'class': 'form-control'}),
        label='Cargo'
    )
    is_checked = forms.BooleanField(
        required=False,
        label="Ativo",
        widget=forms.CheckboxInput(attrs={'class': 'form-check-input'})
    )

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password']
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'})
        }
        labels = {
            'username': 'Username',
            'first_name': 'Primeiro Nome',
            'last_name': 'Último Nome',
            'email': 'Email'
        }
