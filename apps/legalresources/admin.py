from django.contrib import admin
from django.utils.html import format_html
from .models import LegalResource, FavoriteResource

@admin.register(LegalResource)
class LegalResourceAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'created_at', 'image_tag', 'file_link')
    search_fields = ('title',)
    list_filter = ('created_at',)
    ordering = ('id',)

    def image_tag(self, obj):
        if obj.image:
            return format_html(
                '<img src="{}" style="max-height:50px; max-width:50px;" />',
                obj.image.url
            )
        return "-"
    image_tag.short_description = 'Image'
    
    def file_link(self, obj):
        if obj.file:
            return format_html(
                '<a href="{}" target="_blank">Download File</a>',
                obj.file.url
            )
        return "-"
    file_link.short_description = 'File'

@admin.register(FavoriteResource)
class FavoriteResourceAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'resource', 'favorited_at')
    search_fields = ('user__username', 'resource__title')
    list_filter = ('favorited_at',)
