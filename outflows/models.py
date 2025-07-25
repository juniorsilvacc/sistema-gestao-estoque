from django.db import models
from products.models import Product


class Outflow(models.Model):
    REASON_CHOICES = [
        ('venda', 'Venda'),
        ('devolucao', 'Devolução'),
        ('ajuste', 'Ajuste de estoque'),
        ('outro', 'Outro'),
    ]
    
    product = models.ForeignKey(Product, on_delete=models.PROTECT, related_name='outflows', verbose_name='Produto')
    reason = models.CharField("Motivo", max_length=20, choices=REASON_CHOICES, default='venda')
    description = models.TextField("Descrição", null=True, blank=True)
    quantity = models.IntegerField("Quantidade")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    class Meta:
        verbose_name = "Saída"
        verbose_name_plural = "Saídas"
        ordering = ['-created_at']
    
    def __str__(self):
        return str(self.product)
