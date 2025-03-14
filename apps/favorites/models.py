# favorites/models.py

from django.db import models
from django.contrib.auth.models import User
from legalresources.models import LegalResource
from educationalopportunities.models import EducationalOpportunity

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

class FavoriteOpportunity(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='favorite_opportunities'
    )
    opportunity = models.ForeignKey(
        EducationalOpportunity,
        on_delete=models.CASCADE,
        related_name='favorited_by'
    )
    favorited_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'opportunity')
        ordering = ('-favorited_at',)

    def __str__(self):
        return f"{self.user.username} - {self.opportunity.title}"
