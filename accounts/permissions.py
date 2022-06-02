from rest_framework import permissions


class IsAdminOrLoggedInUser(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        is_logged_in_user = obj == request.user
        is_admin = request.user.is_superuser

        if request.method == 'POST':
            return True
        elif is_logged_in_user or is_admin:
            return True

        return False


class IsNotAuthenticated(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.user.is_authenticated:
            return False
        return True
