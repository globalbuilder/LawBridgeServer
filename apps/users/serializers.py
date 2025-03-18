# users/serializers.py
from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Profile

class UserSerializer(serializers.ModelSerializer):
    """Read-only serializer for the User model."""
    class Meta:
        model = User
        fields = ['id', 'username', 'first_name', 'last_name', 'email']
        read_only_fields = ['id', 'username']

class ProfileSerializer(serializers.ModelSerializer):
    """
    Flattened serializer for Profile that includes user fields at the same level.
    So we expect JSON like:
        {
          "first_name": "...",
          "last_name": "...",
          "email": "...",
          "phone": "...",
          "address": "...",
          "bio": "...",
          "image": ...
        }
    """
    first_name = serializers.CharField(required=False)
    last_name = serializers.CharField(required=False)
    email = serializers.EmailField(required=False, allow_blank=True, allow_null=True)

    class Meta:
        model = Profile
        fields = [
            'id',
            'first_name',
            'last_name',
            'email',
            'phone',
            'address',
            'image',
            'bio'
        ]
        read_only_fields = ['id']

    def update(self, instance, validated_data):
        user = instance.user
        
        # Extract user-related fields if present
        if 'first_name' in validated_data:
            user.first_name = validated_data.pop('first_name')
        if 'last_name' in validated_data:
            user.last_name = validated_data.pop('last_name')
        if 'email' in validated_data:
            user.email = validated_data.pop('email')
        
        user.save()  # Save any user changes

        # Now update the Profile fields normally
        return super().update(instance, validated_data)

class RegisterSerializer(serializers.ModelSerializer):
    """
    Serializer for user registration.
    Required fields: username, password, first_name, last_name.
    Optional: image (to be saved in Profile).
    """
    password = serializers.CharField(write_only=True)
    image = serializers.ImageField(write_only=True, required=False)

    class Meta:
        model = User
        fields = ['username', 'password', 'first_name', 'last_name', 'image']

    def create(self, validated_data):
        image = validated_data.pop('image', None)  # Optional image
        password = validated_data.pop('password')
        user = User.objects.create(**validated_data)
        user.set_password(password)
        user.save()
        # If an image was provided, set it on the profile
        if image:
            user.profile.image = image
            user.profile.save()
        return user
