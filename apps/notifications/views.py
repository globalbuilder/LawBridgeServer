# notifications/views.py

from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from django.db.models import Q
from .models import Notification
from .serializers import NotificationSerializer
from .permissions import IsAdminOrReadOnlyNotification

class NotificationViewSet(viewsets.ModelViewSet):
    serializer_class = NotificationSerializer
    permission_classes = [IsAuthenticated, IsAdminOrReadOnlyNotification]

    def get_queryset(self):
        # Admin users see all notifications.
        if self.request.user.is_staff:
            return Notification.objects.all().order_by('-created_at')
        # Normal users see broadcast notifications or those addressed specifically to them.
        return Notification.objects.filter(
            Q(is_broadcast=True) | Q(user=self.request.user)
        ).order_by('-created_at')
