from django.contrib import admin
from . import models


class InflowAdmin(admin.ModelAdmin):
    list_display = ('supplier', 'product', 'purchase_price', 'invoice_number', 'quantity', 'description',)
    search_fields = ('supplier__name', 'product__title')

admin.site.register(models.Inflow, InflowAdmin)
