from rest_framework import permissions

class UserPermission(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if view.action in ('list', 'create', 'retrieve'):
            return True
        return obj == request.user

class ExerciseSessionPermission(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if view.action in ('list', 'retrieve'):
            return True

        if view.action == 'create':
            return request.user.is_authenticated

        return obj.user == request.user
