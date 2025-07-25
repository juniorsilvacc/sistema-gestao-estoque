from django.db import models

class Brand(models.Model):
    name = models.CharField("Nome", max_length=500)
    website = models.URLField("Website", null=True, blank=True)
    description = models.TextField("Descrição", null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    class Meta:
        verbose_name = "Marca"
        verbose_name_plural = "Marcas"
        ordering = ['-created_at']
    
    def __str__(self):
        return self.name