from django.db import models
from brands.models import Brand
from categories.models import Category
import random


class Product(models.Model):
    title = models.CharField("Título", max_length=500)
    category = models.ForeignKey(Category, on_delete=models.PROTECT, related_name='products', verbose_name="Categoria")
    brand = models.ForeignKey(Brand, on_delete=models.PROTECT, related_name='products', verbose_name="Marca")
    description = models.TextField("Descrição", null=True, blank=True)
    serie_number = models.CharField("Número de Série", max_length=200, null=True, blank=True)
    internal_code = models.CharField("Código Interno", max_length=20, unique=True)
    cost_price = models.DecimalField("Preço de Custo", max_digits=20, decimal_places=2)
    selling_price = models.DecimalField("Preço de Venda", max_digits=20, decimal_places=2)
    quantity = models.IntegerField("Quantidade", default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    class Meta:
        verbose_name = "Produto"
        verbose_name_plural = "Produtos"
        ordering = ['-created_at']
    
    def __str__(self):
        return self.title
    
    def gerar_codigo(self):
        return str(random.randint(10**12, 10**13 - 1))
