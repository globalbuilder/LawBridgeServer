# legalresources/models.py

from django.db import models
from accounts.models import User

class LegalResource(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    file = models.FileField(upload_to='legal_resources/', blank=True, null=True)
    image = models.ImageField(upload_to='legal_resources/images/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class FavoriteResource(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='favorite_resources'
    )
    resource = models.ForeignKey(
        LegalResource,
        on_delete=models.CASCADE,
        related_name='favorited_by'
    )
    favorited_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'resource')
        ordering = ('-favorited_at',)

    def __str__(self):
        return f"{self.user.username} - {self.resource.title}"