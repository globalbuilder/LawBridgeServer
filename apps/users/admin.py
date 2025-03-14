# users/admin.py

from django.contrib import admin
from django.contrib.auth.models import User
from .models import Profile
from django.utils.html import format_html

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('id', 'user_username', 'user_full_name', 'phone', 'preview_image')
    list_filter = ('user__is_staff', 'user__is_active')
    ordering = ('id',)

    def user_username(self, obj):
        return obj.user.username
    user_username.short_description = "Username"

    def user_full_name(self, obj):
        return f"{obj.user.first_name} {obj.user.last_name}"
    user_full_name.short_description = "Full Name"

    def preview_image(self, obj):
        if obj.image:
            return format_html(
                "<img src='{}' style='max-height:50px; max-width:50px;' />",
                obj.image.url
            )
        return "No Image"
    preview_image.short_description = "Profile Picture"
