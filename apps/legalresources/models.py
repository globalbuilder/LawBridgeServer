# legalresources/models.py

from django.db import models

class LegalResource(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    file = models.FileField(upload_to='legal_resources/', blank=True, null=True)
    image = models.ImageField(upload_to='legal_resources/images/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
