from django.db import models
from accounts.models import User

class EducationalOpportunity(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    start_date = models.DateTimeField(blank=True, null=True)
    end_date = models.DateTimeField(blank=True, null=True)
    location = models.CharField(max_length=255, blank=True, null=True)
    contact_info = models.CharField(max_length=255, blank=True, null=True)
    external_link = models.URLField(blank=True, null=True)
    image = models.ImageField(upload_to='educational_opportunities/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

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