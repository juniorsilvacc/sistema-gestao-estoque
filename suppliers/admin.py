from django.contrib import admin
from . import models


class SupplierAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'cnpj', 'cellphone', 'phone', 'is_whatsapp', 'cep', 'street', 
                'number', 'neighborhood', 'city', 'state', 'complement', 'description',)
    search_fields = ('name', 'cnpj',)

admin.site.register(models.Supplier, SupplierAdmin)
