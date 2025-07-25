from django.db import models


class StateChoices(models.TextChoices):
    AC = 'AC', 'Acre'
    AL = 'AL', 'Alagoas'
    AP = 'AP', 'Amapá'
    AM = 'AM', 'Amazonas'
    BA = 'BA', 'Bahia'
    CE = 'CE', 'Ceará'
    DF = 'DF', 'Distrito Federal'
    ES = 'ES', 'Espírito Santo'
    GO = 'GO', 'Goiás'
    MA = 'MA', 'Maranhão'
    MT = 'MT', 'Mato Grosso'
    MS = 'MS', 'Mato Grosso do Sul'
    MG = 'MG', 'Minas Gerais'
    PA = 'PA', 'Pará'
    PB = 'PB', 'Paraíba'
    PR = 'PR', 'Paraná'
    PE = 'PE', 'Pernambuco'
    PI = 'PI', 'Piauí'
    RJ = 'RJ', 'Rio de Janeiro'
    RN = 'RN', 'Rio Grande do Norte'
    RS = 'RS', 'Rio Grande do Sul'
    RO = 'RO', 'Rondônia'
    RR = 'RR', 'Roraima'
    SC = 'SC', 'Santa Catarina'
    SP = 'SP', 'São Paulo'
    SE = 'SE', 'Sergipe'
    TO = 'TO', 'Tocantins'

class Supplier(models.Model):
    name = models.CharField("Nome", max_length=500)
    email = models.EmailField("Email", max_length=255, null=True, blank=True)
    cnpj = models.CharField("CNPJ", max_length=18, null=True, blank=True)
    cellphone = models.CharField("Celular", max_length=20, null=True, blank=True)
    phone = models.CharField("Telefone", max_length=20, null=True, blank=True)
    is_whatsapp = models.BooleanField("É WhatsApp?", default=False)
    cep = models.CharField("CEP", max_length=9, null=True, blank=True)
    street = models.CharField("Rua", max_length=255, null=True, blank=True)
    number = models.CharField("Número", max_length=10, null=True, blank=True)
    neighborhood = models.CharField("Bairro", max_length=100, null=True, blank=True)
    city = models.CharField("Cidade", max_length=100, null=True, blank=True)
    state = models.CharField("Estado", max_length=2, choices=StateChoices.choices, null=True, blank=True)
    complement = models.CharField("Complemento", max_length=255, null=True, blank=True)
    description = models.TextField("Descrição", null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    class Meta:
        verbose_name = "Fornecedor"
        verbose_name_plural = "Fornecedores"
        ordering = ['-created_at']
    
    def __str__(self):
        return self.name
