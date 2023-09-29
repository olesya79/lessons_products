from lessons.api.v1.views.lesson_view import LessonViewSet
from lessons.api.v1.views.lesson_view import ProductViewSet
from products.api.v1.views.owner_view import OwnerViewSet
from products.api.v1.views.product_view import ProductStatsAPIView
from users.api.v1.views.user_view import UserViewSet
from rest_framework import routers
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'lessons', LessonViewSet,  basename='lesson')
router.register(r'products', ProductViewSet, basename='product')
router.register(r'owner', OwnerViewSet, basename='owner')
router.register(r'user', UserViewSet, basename='user')

urlpatterns = router.urls