from rest_framework import permissions

from apps.models import Vacancy


class IsOwner(permissions.BasePermission):
    def has_object_permission(self, request, view, obj: Vacancy):
        return request.user == obj.user and request.user.is_authenticated

