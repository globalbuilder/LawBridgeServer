# users/permissions.py

from rest_framework import permissions

class IsOwnerOrReadOnlyProfile(permissions.BasePermission):
    """
    Only allow a user to update their own profile.
    """
    def has_object_permission(self, request, view, obj):
        # Allow safe methods (GET, HEAD, OPTIONS) only for the owner.
        if request.method in permissions.SAFE_METHODS:
            return obj.user == request.user
        # For modifications, ensure the requesting user is the owner.
        return obj.user == request.user
