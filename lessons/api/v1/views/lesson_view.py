from lessons.api.v1.serializers.lessons_serializers import LessonSerializer
from lessons.models import Lesson
from products.models import Product
from rest_framework import viewsets
from core.permissions import IsAuthenticated
from products.api.v1.serializers.product_serializer import ProductSerializer


class LessonViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = LessonSerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        user = self.request.user
        return Lesson.objects.filter(product__lessons=user)

class ProductViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = ProductSerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        user = self.request.user
        return Product.objects.filter(lessons=user)

