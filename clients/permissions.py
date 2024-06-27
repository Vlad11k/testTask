from rest_framework import permissions


class IsEmployee(permissions.BasePermission):
    def has_permission(self, request, view):
        try:
            return bool(request.user.is_staff or request.user.employee)
        except:
            return False
