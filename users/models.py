from django.contrib.auth.models import User
from django.db import models

class Profile(models.Model):
    ROLE_CHOICES = [
        ('admin', 'Administrador'),
        ('manager', 'Gerente'),
        ('user', 'Usuário'),
    ]

    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name="Usuário")
    role = models.CharField("Cargo", max_length=20, choices=ROLE_CHOICES, default='user')
    is_checked = models.BooleanField("Ativo?", default=True)

    class Meta:
        verbose_name = "Perfil"
        verbose_name_plural = "Perfis"

    def __str__(self):
        return f"{self.user.username} ({self.role})"
