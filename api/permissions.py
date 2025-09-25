# permissions.py

from rest_framework.permissions import BasePermission

class IsSuperAdminOrReadOnly(BasePermission):
    """
    Superadmin uchun barcha CRUD amallari ruxsat etiladi.
    Boshqa foydalanuvchilarga faqat GET va POST ruxsat etiladi.
    """
    def has_permission(self, request, view):
        # Agar foydalanuvchi superadmin bo'lsa, barcha CRUD amallari ruxsat etiladi
        if request.user and request.user.is_superuser:
            return True

        # Boshqa foydalanuvchilarga faqat GET va POST ruxsat etiladi
        if request.method in ['GET', 'POST']:
            return True

        return False
