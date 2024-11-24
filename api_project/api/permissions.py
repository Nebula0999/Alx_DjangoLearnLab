from rest_framework.permissions import BasePermission

class IsEditor(BasePermission):
    """
    Custom permission to grant access only to users in the 'Editors' group.
    """
    def has_permission(self, request, view):
        return request.user and request.user.groups.filter(name='Editors').exists()