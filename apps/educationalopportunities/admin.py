from django.contrib import admin
from django.utils.html import format_html
from .models import EducationalOpportunity, FavoriteOpportunity

@admin.register(EducationalOpportunity)
class EducationalOpportunityAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'start_date', 'end_date', 'location', 'created_at', 'image_tag')
    search_fields = ('title', 'location')
    list_filter = ('start_date', 'end_date', 'created_at')

    def image_tag(self, obj):
        if obj.image:
            return format_html(
                '<img src="{}" style="max-height:50px; max-width:50px;" />',
                obj.image.url
            )
        return "-"
    image_tag.short_description = 'Image'

@admin.register(FavoriteOpportunity)
class FavoriteOpportunityAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'opportunity', 'favorited_at')
    search_fields = ('user__username', 'opportunity__title')
    list_filter = ('favorited_at',)
