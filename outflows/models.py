from django.db import models
from products.models import Product


REASON_CHOICES = [
    ('venda', 'Venda'),
    ('devolucao', 'Devolução'),
    ('ajuste', 'Ajuste de estoque'),
    ('outro', 'Outro'),
]

class Outflow(models.Model):
    product = models.ForeignKey(Product, on_delete=models.PROTECT, related_name='outflows')
    reason = models.CharField(max_length=20, choices=REASON_CHOICES, default='venda')
    description = models.TextField(null=True, blank=True)
    quantity = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    class Meta:
        ordering = ['-created_at']
    
    def __str__(self):
        return str(self.product)
