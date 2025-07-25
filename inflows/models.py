from django.db import models
from suppliers.models import Supplier
from products.models import Product

class Inflow(models.Model):
    supplier = models.ForeignKey(Supplier, on_delete=models.PROTECT, related_name='inflows', verbose_name='Fornecedor')
    product = models.ForeignKey(Product, on_delete=models.PROTECT, related_name='inflows', verbose_name='Produto')
    purchase_price = models.DecimalField("Preço de Compra", max_digits=10, decimal_places=2, null=True, blank=True)
    invoice_number = models.PositiveIntegerField("Número da Nota Fiscal", blank=True, null=True)
    quantity = models.IntegerField("Quantidade")
    description = models.TextField("Observações", null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    class Meta:
        verbose_name = "Entrada"
        verbose_name_plural = "Entradas"
        ordering = ['-created_at']

    def __str__(self):
        return str(self.product)
