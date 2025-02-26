from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r'matches', views.MatchViewSet, basename='match')

urlpatterns = [
    path('', include(router.urls)),
    path('matched-profiles/', views.MatchViewSet.as_view({'get': 'profiles'}), name='matched-profiles'),
    path('matched-profile-ids/', views.MatchViewSet.as_view({'get': 'profile_ids'}), name='matched-profile-ids'),
]
