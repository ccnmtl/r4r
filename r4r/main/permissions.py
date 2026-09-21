from rest_framework.permissions import (
    BasePermission, IsAuthenticated, DjangoModelPermissionsOrAnonReadOnly,
    SAFE_METHODS
)


class DjangoModelPermissionsOrAuthReadOnly(
        DjangoModelPermissionsOrAnonReadOnly):
    authenticated_users_only = True


class IsSuperuserOrReadOnlyAuth(IsAuthenticated):
    """
    Authenticated users below superuser have read-only access
    """

    def has_permission(self, request, view):
        if request.method in SAFE_METHODS:
            return True

        return bool(request.user.is_superuser)


class IsStaffOrReadOnlyAuth(BasePermission):
    """
    Authenticated users below superuser have read-only access
    """

    def has_permission(self, request, view):
        if request.method in SAFE_METHODS:
            return True

        return bool(request.user.is_staff)


class ReadOnly(BasePermission):
    """
    For views that aren't supposed to modify data
    """

    def has_permission(self, request, view):
        return bool(request.method in SAFE_METHODS)


class IsStaffOrSelf(IsAuthenticated):
    def has_permission(self, request, view):
        if request.user.is_staff:
            return True
        elif request.method in SAFE_METHODS:
            pass
        else:
            return False
