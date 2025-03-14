# favorites/serializers.py

from rest_framework import serializers
from .models import FavoriteResource, FavoriteOpportunity

class FavoriteResourceSerializer(serializers.ModelSerializer):
    class Meta:
        model = FavoriteResource
        fields = ['id', 'resource', 'favorited_at']
        read_only_fields = ['id', 'favorited_at']

class FavoriteOpportunitySerializer(serializers.ModelSerializer):
    class Meta:
        model = FavoriteOpportunity
        fields = ['id', 'opportunity', 'favorited_at']
        read_only_fields = ['id', 'favorited_at']
