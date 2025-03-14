# legalresources/permissions.py

from rest_framework import permissions

class IsAdminOrReadOnly(permissions.BasePermission):
    """
    Custom permission to allow admin users to create, update, or delete resources.
    Non-admin users have read-only access.
    """

    def has_permission(self, request, view):
        # Allow read-only methods for any request
        if request.method in permissions.SAFE_METHODS:
            return True
        # Otherwise, only allow if the user is an admin (staff)
        return request.user and request.user.is_staff

    def has_object_permission(self, request, view, obj):
        # Read-only for safe methods; admin for changes
        if request.method in permissions.SAFE_METHODS:
            return True
        return request.user and request.user.is_staff
