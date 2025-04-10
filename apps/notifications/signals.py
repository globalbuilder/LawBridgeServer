from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth import get_user_model

from educationalopportunities.models import EducationalOpportunity
from legalresources.models import LegalResource
from .models import Notification

User = get_user_model()

@receiver(post_save, sender=EducationalOpportunity)
def create_notification_for_new_opportunity(sender, instance, created, **kwargs):
    if created:
        active_users = User.objects.filter(is_active=True)
        title = "New Educational Opportunity"
        message = f"A new educational opportunity '{instance.title}' has been added."
        notifications = []
        for user in active_users:
            notifications.append(
                Notification(
                    user=user,
                    title=title,
                    message=message
                )
            )
        Notification.objects.bulk_create(notifications)  

@receiver(post_save, sender=LegalResource)
def create_notification_for_new_legal_resource(sender, instance, created, **kwargs):
    if created:
        active_users = User.objects.filter(is_active=True)
        title = "New Legal Resource"
        message = f"A new legal resource '{instance.title}' has been added."
        notifications = []
        for user in active_users:
            notifications.append(
                Notification(
                    user=user,
                    title=title,
                    message=message
                )
            )
        Notification.objects.bulk_create(notifications)
