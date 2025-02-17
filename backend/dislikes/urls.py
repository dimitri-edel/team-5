from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r'dislikes', views.DislikeViewSet, basename='dislike')

urlpatterns = [
    path('', include(router.urls)),
]
