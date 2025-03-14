# notifications/models.py

from django.db import models
from django.contrib.auth.models import User


class Notification(models.Model):
    title = models.CharField(max_length=255)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    is_broadcast = models.BooleanField(default=False)
    # For single-user notifications (if not broadcast)
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name='notifications'
    )
    # Optional reference to a LegalResource that triggered this notification
    resource = models.ForeignKey(
        'legalresources.LegalResource',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='notifications'
    )
    # Optional reference to an EducationalOpportunity that triggered this notification
    opportunity = models.ForeignKey(
        'educationalopportunities.EducationalOpportunity',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='notifications'
    )

    def __str__(self):
        if self.is_broadcast:
            return f"[Broadcast] {self.title}"
        else:
            return f"[To {self.user.username}] {self.title}"
