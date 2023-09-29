from django.contrib import admin
from django.urls import path, re_path, include
import products
from core.urls import router


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include(router.urls)),
    path('api/statistics/', products.api.v1.views.product_view.ProductStatsAPIView.as_view(), name="statistics"),
    path('api/v1/auth/', include('djoser.urls')),
    re_path(r'^auth/', include('djoser.urls.authtoken')),
]

