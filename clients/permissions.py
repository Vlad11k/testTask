from rest_framework import permissions


# class IsOwner(permissions.BasePermission):
#     def has_object_permission(self, request, view, obj):
#         client = obj.user_ptr
#         user = request.user
#         return client == user


class IsEmployee(permissions.BasePermission):
    def has_permission(self, request, view):
        try:
            return bool(request.user.is_staff or request.user.employee)
        except:
            return False
