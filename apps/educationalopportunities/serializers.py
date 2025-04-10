from rest_framework import serializers
from .models import EducationalOpportunity, FavoriteOpportunity

class EducationalOpportunitySerializer(serializers.ModelSerializer):
    class Meta:
        model = EducationalOpportunity
        fields = [
            'id',
            'title',
            'description',
            'start_date',
            'end_date',
            'location',
            'contact_info',
            'external_link',
            'image',
            'created_at',
            'updated_at',
        ]

class FavoriteOpportunitySerializer(serializers.ModelSerializer):

    opportunity = EducationalOpportunitySerializer(read_only=True)

    class Meta:
        model = FavoriteOpportunity
        fields = [
            'id',
            'opportunity',
            'favorited_at',
        ]
