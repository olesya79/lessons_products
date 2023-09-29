from products.api.v1.serializers.owner_serializer import OwnerSerializer
from products.models import Owner
from rest_framework import viewsets
from core.permissions import IsOwnerOrReadOnly


class OwnerViewSet(viewsets.ModelViewSet):
    queryset = Owner.objects.all()
    serializer_class = OwnerSerializer
    permission_classes = (IsOwnerOrReadOnly,)
