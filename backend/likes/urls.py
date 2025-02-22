from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import LikeViewSet

router = DefaultRouter()
router.register(r'', LikeViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('notifications/', LikeViewSet.as_view({'get': 'notifications'}), name='notifications'),
]
