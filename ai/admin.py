from django.contrib import admin
from ai import models


class AIResultAdmin(admin.ModelAdmin):
    list_display = ('result', 'created_at',)

admin.site.register(models.APIResult, AIResultAdmin)