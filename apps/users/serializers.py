# users/serializers.py

from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Profile

class UserSerializer(serializers.ModelSerializer):
    """Serializer for the User model. Username is read-only."""
    class Meta:
        model = User
        fields = ['id', 'username', 'first_name', 'last_name', 'email']
        read_only_fields = ['id', 'username']

class ProfileSerializer(serializers.ModelSerializer):
    """
    Serializer for Profile that allows updating of the nested User fields:
    first_name, last_name, and email.
    """
    # Declare these fields so we can update them directly.
    first_name = serializers.CharField(source='user.first_name')
    last_name = serializers.CharField(source='user.last_name')
    email = serializers.EmailField(source='user.email', required=False, allow_blank=True)

    class Meta:
        model = Profile
        fields = ['id', 'first_name', 'last_name', 'email', 'phone', 'address', 'image', 'bio']
        read_only_fields = ['id']

    def update(self, instance, validated_data):
        # Extract nested user data
        user_data = validated_data.pop('user', {})
        user = instance.user
        user.first_name = user_data.get('first_name', user.first_name)
        user.last_name = user_data.get('last_name', user.last_name)
        user.email = user_data.get('email', user.email)
        user.save()
        # Update the Profile fields
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
        # Profile is auto-created via signal; update image if provided.
        if image:
            user.profile.image = image
            user.profile.save()
        return user
