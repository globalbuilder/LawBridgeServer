# notifications/signals.py

from django.db.models.signals import post_save
from django.dispatch import receiver
from legalresources.models import LegalResource
from educationalopportunities.models import EducationalOpportunity
from .models import Notification

@receiver(post_save, sender=LegalResource)
def create_legalresource_notification(sender, instance, created, **kwargs):
    if created:
        Notification.objects.create(
            title="New Legal Resource Posted",
            message=f"A new legal resource '{instance.title}' has been added.",
            is_broadcast=True,
            resource=instance
        )

@receiver(post_save, sender=EducationalOpportunity)
def create_educationalopportunity_notification(sender, instance, created, **kwargs):
    if created:
        Notification.objects.create(
            title="New Educational Opportunity",
            message=f"A new educational opportunity '{instance.title}' is available.",
            is_broadcast=True,
            opportunity=instance
        )
