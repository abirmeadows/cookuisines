from rest_framework import permissions


class isOwnerOrReadOnly(permissions.BasePermission):
    message = "You are not the owner of the object"

    def has_object_permission(self, request, view, obj):
        if(request.method in permissions.SAFE_METHODS):
            return True

        return obj.creator == request.user
