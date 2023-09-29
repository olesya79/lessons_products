from rest_framework import viewsets

from users.api.v1.serializers.user_serializer import UserSerializer
from users.models import User
from core.permissions import AllowAny


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    search_fields = ['first_name', 'second_name']
    permission_classes = (AllowAny,)