from rest_framework import serializers
from .models import EducationalOpportunity

class EducationalOpportunitySerializer(serializers.ModelSerializer):
    class Meta:
        model = EducationalOpportunity
        fields = '__all__'
        read_only_fields = ('created_at', 'updated_at')
