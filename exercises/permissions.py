from rest_framework import permissions

class UserPermission(permissions.BasePermission):
    def has_permission(self, request, view):
        if view.action in ('list', 'retrieve', 'create'):
            return True

        if view.action in ('update', 'partial_update', 'destroy'):
            return request.user.is_authenticated

        return False

    def has_object_permission(self, request, view, obj):
        if view.action == 'retrieve':
            return True
        
        return obj == request.user

class ExerciseSessionPermission(permissions.BasePermission):
    def has_permission(self, request, view):
        if view.action in ('list', 'retrieve'):
            return True

        return request.user.is_authenticated

    def has_object_permission(self, request, view, obj):
        if view.action == 'retrieve':
            return True

        if view.action == 'create':
            return request.user.is_authenticated

        return obj.user == request.user
