from django.db import models


class APIResult(models.Model):
    result = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering= ['-created_at']