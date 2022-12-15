from rest_framework import permissions
from rest_framework.permissions import SAFE_METHODS, BasePermission


class Not_2y(permissions.BasePermission):
    message = 'You are not matured enough ... lol'

    def has_permission(self, request, view):
        if request.user.is_authenticated:
            if request.user.year > 1:  # 2
                return True

        return False


class can_3y_and_2y_view(BasePermission):
    message = 'You are not matured enough ... lol'

    def has_permission(self, request, view):
        if request.user.is_authenticated:
            if request.user.year > 1:  # 3
                return True
            if request.method in SAFE_METHODS:
                return True
        return False
