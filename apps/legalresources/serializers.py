from rest_framework import serializers
from .models import LegalResource, FavoriteResource

class LegalResourceSerializer(serializers.ModelSerializer):
    class Meta:
        model = LegalResource
        fields = [
            'id',
            'title',
            'description',
            'file',
            'image',
            'created_at',
            'updated_at',
        ]

class FavoriteResourceSerializer(serializers.ModelSerializer):

    resource = LegalResourceSerializer(read_only=True)

    class Meta:
        model = FavoriteResource
        fields = [
            'id',
            'resource',
            'favorited_at',
        ]
