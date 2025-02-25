from django.urls import path, include
from .views import LikeViewSet

urlpatterns = [
    path('like/<int:pk>/', LikeViewSet.as_view({'post': 'like'}), name='likeendpoint'),
    path('notifications/', LikeViewSet.as_view({'get': 'notifications'}), name='notifications'),
]
