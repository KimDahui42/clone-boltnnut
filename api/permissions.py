from django.contrib.auth import get_user_model
from rest_framework.permissions import BasePermission, SAFE_METHODS

class IsOwnerOnly(BasePermission):
    def has_permission(self, request, view):
        if request.user.is_authenticated:
            return True
        return False

class IsPartner(BasePermission):
    def has_permission(self, request, view):
        if view.action == 'list':
            return True
        elif view.action == 'create':
            return True
        elif view.action in ['retrieve', 'update', 'partial_update']:
            return True
        else:
            return False

    def has_object_permission(self, request, view, obj):
        # Deny actions on objects if the user is not authenticated
        if view.action == 'retrieve':
            return True
        elif view.action in ['update', 'partial_update']:
            return request.user.id==obj.profile.id or request.user.is_admin
        else:
            return False
