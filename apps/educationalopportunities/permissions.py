from rest_framework import permissions

class IsAdminOrReadOnly(permissions.BasePermission):
    """
    Custom permission to allow only admin users to modify educational opportunities.
    All users have read-only access.
    """

    def has_permission(self, request, view):
        # Allow read-only methods for any request.
        if request.method in permissions.SAFE_METHODS:
            return True
        # For write methods, allow only if user is an admin (staff).
        return request.user and request.user.is_staff

    def has_object_permission(self, request, view, obj):
        # Read-only is allowed for any request.
        if request.method in permissions.SAFE_METHODS:
            return True
        # Write permissions are only allowed for admin users.
        return request.user and request.user.is_staff
