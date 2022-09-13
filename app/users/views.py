from rest_framework.permissions import IsAuthenticated
from rest_framework import status, viewsets

from typing import Union, List
from users.models import User
from .serializers import UserModelSerializer


class UserViewSet(viewsets.ModelViewSet):
    """
    A simple viewset for User model
    """
    queryset = User.objects.all()
    serializer_class = UserModelSerializer

    def get_permissions(self) -> List:
        """
        Return the list of permissions that will apply to API endpoints.
        Personally, I want to grant access to POST method to unauthenticated users below.
        :return:
        """
        permission_classes_ = []
        if self.action != "create":
            permission_classes_ = [IsAuthenticated]
        return [permission() for permission in permission_classes_]
