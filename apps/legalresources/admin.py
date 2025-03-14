# legalresources/admin.py

from django.contrib import admin
from django.utils.html import format_html
from .models import LegalResource

@admin.register(LegalResource)
class LegalResourceAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'preview_image', 'file_link', 'created_at')
    list_filter = ('created_at',)
    ordering = ('-created_at',)

    def preview_image(self, obj):
        if obj.image:
            return format_html(
                "<img src='{}' style='max-height:50px; max-width:50px;'/>", 
                obj.image.url
            )
        return "No Image"
    preview_image.short_description = "Image Preview"

    def file_link(self, obj):
        if obj.file:
            return format_html(
                "<a href='{}' target='_blank'>Open PDF</a>", 
                obj.file.url
            )
        return "No File"
    file_link.short_description = "PDF File"
