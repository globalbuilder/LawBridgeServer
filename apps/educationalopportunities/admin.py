# educationalopportunities/admin.py

from django.contrib import admin
from django.utils.html import format_html
from .models import EducationalOpportunity

@admin.register(EducationalOpportunity)
class EducationalOpportunityAdmin(admin.ModelAdmin):
    list_display = (
        'id', 
        'title', 
        'preview_image', 
        'external_link_display', 
        'start_date', 
        'end_date', 
        'created_at'
    )
    list_filter = ('start_date', 'end_date',)
    ordering = ('-created_at',)

    def preview_image(self, obj):
        if obj.image:
            return format_html(
                "<img src='{}' style='max-height:50px; max-width:50px;'/>", 
                obj.image.url
            )
        return "No Image"
    preview_image.short_description = "Image Preview"

    def external_link_display(self, obj):
        if obj.external_link:
            return format_html(
                "<a href='{}' target='_blank'>Open Link</a>", 
                obj.external_link
            )
        return "No Link"
    external_link_display.short_description = "External Link"
