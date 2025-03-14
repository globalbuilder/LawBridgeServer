# notifications/admin.py

from django.contrib import admin
from .models import Notification

@admin.register(Notification)
class NotificationAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'is_broadcast', 'user_display', 'created_at')
    list_filter = ('is_broadcast', 'created_at')
    ordering = ('-created_at',)

    def user_display(self, obj):
        return obj.user.username if obj.user else "Broadcast"
    user_display.short_description = "User"
