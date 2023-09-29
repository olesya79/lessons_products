from rest_framework.views import APIView
from rest_framework.response import Response
from products.models import Product
from products.api.v1.serializers.product_serializer import ProductSerializer
from core.permissions import IsAdminOrReadOnly
from rest_framework import viewsets
from lessons.models import Lesson, LessonView
from users.models import User
from django.db import models


class ProductStatsAPIView(APIView):
    def get(self, request):
        queryset = Product.objects.all()
        num_total_lessons_viewed = LessonView.objects.filter(status='Viewed').count()
        total_view_time = LessonView.objects.aggregate(models.Sum('view_time'))
        permission_classes = (IsAdminOrReadOnly,)

        data = []
        for product in products:
            num_lessons_viewed = Lesson.objects.filter(lesson__in=product.lesson_set.all()).count()
            total_lesson_time = Lesson.objects.filter(lesson__in=product.lesson_set.all()).aggregate(models.Sum('lesson__duration'))
            num_enrolled_users = User.objects.filter(lessonview__lesson__products=product).distinct().count()

            percentage_of_access = num_enrolled_users / User.objects.all().count() * 100

            product_data = {
                'product': ProductSerializer(product).data,
                'num_lessons_viewed': num_lessons_viewed,
                'total_lesson_time': total_lesson_time,
                'num_enrolled_users': num_enrolled_users,
                'percentage_of_access': percentage_of_access
            }
            data.append(product_data)

        return Response(data)