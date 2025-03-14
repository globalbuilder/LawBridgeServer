# legalresources/serializers.py

from rest_framework import serializers
from .models import LegalResource

class LegalResourceSerializer(serializers.ModelSerializer):
    class Meta:
        model = LegalResource
        fields = '__all__'
        read_only_fields = ('created_at', 'updated_at')
