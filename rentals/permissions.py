from rest_framework import permissions


class IsAdminOrOwner(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        is_logged_in_user = obj.user == request.user
        is_admin = request.user.is_superuser

        if request.method == 'POST':
            return True
        elif is_logged_in_user or is_admin:
            return True

        return False
