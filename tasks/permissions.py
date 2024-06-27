from rest_framework import permissions


class IsOwner(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.user.is_staff:
            return True

        pk = request.user.pk
        return pk == obj.client_id or pk == obj.employee_id
