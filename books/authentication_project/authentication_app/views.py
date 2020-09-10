from rest_framework import viewsets
from .models import Book
from .serializers import BookSerializers
from rest_framework import permissions
from rest_framework.exceptions import PermissionDenied

"""This class gives permissions to the requested user"""
class IsOwner(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj.owner == request.user


class BookViewset(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializers

    def get_queryset(self):
        user = self.request.user
        if user.is_authenticated:
            return Book.objects.filter(owner=user)
        raise PermissionDenied()
    '''the above method is overriding method it get the requested user and authenticate if not permission is denied'''

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    '''save requested user in bookserializers'''

