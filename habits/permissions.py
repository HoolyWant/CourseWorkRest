from rest_framework.permissions import BasePermission


class ViewSetPermission(BasePermission):
    def has_permission(self, request, view):
        if request.user.is_authenticated:
            if view.action == 'list':
                return True
            elif view.action == 'create':
                if request.user == request.user.is_staff and request.user != request.user.is_superuser:
                    return False
                return True
            elif view.action == 'delete':
                return request.user == view.get_object().user
            elif view.action in ['retrieve', 'update', 'partial_update', ] and request.user == view.get_object(
            ).user or request.user == request.user.is_staff:
                return True
            else:
                return False
        else:
            return False


