from rest_framework import permissions

class IsSuperAdminOrReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.user and request.user.is_superuser:
            return True
        if request.method in ['POST', 'GET']:
            return True
        return False

    def has_object_permission(self, request, view, obj):
        if request.user and request.user.is_superuser:
            return True
        if request.method in ['POST', 'GET']:
            return True
        return False
