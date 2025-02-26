from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r'dislikes', views.DislikeViewSet, basename='dislike')

urlpatterns = [
   path('dislike/<int:pk>/', views.DislikeViewSet.as_view({'post': 'dislike'}), name='dislikeendpoint'),
   path('disliked-profiles/', views.DislikeViewSet.as_view({'get': 'disliked_profiles'}), name='disliked-profiles'),
]
