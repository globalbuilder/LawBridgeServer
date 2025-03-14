# legalresources/admin.py

from django.contrib import admin
from .models import LegalResource
from django.utils.html import format_html

@admin.register(LegalResource)
class LegalResourceAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'preview_image', 'created_at')
    list_filter = ('created_at',)
    ordering = ('-created_at',)

    def preview_image(self, obj):
        if obj.image:
            return format_html(
                "<img src='{}' style='max-height:50px; max-width:50px;' />",
                obj.image.url
            )
        return "No Image"
    preview_image.short_description = "Image Preview"
