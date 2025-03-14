# favorites/admin.py

from django.contrib import admin
from .models import FavoriteResource, FavoriteOpportunity

@admin.register(FavoriteResource)
class FavoriteResourceAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'resource', 'favorited_at')
    list_filter = ('user', 'favorited_at')
    ordering = ('-favorited_at',)

@admin.register(FavoriteOpportunity)
class FavoriteOpportunityAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'opportunity', 'favorited_at')
    list_filter = ('user', 'favorited_at')
    ordering = ('-favorited_at',)
