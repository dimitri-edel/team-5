from rest_framework import viewsets, permissions, generics
from django_filters import rest_framework as filters
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.pagination import PageNumberPagination
from .models import UserProfile
from .serializers import UserProfileSerializer
from .filters import UserProfileFilter
from .pagination import UserProfilePagination

class UserProfileViewSet(viewsets.ModelViewSet):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = UserProfileFilter
    pagination_class = UserProfilePagination

    def get_queryset(self):
        user = self.request.user
        queryset = UserProfile.objects.all()
        if self.action == 'list':            
            # Exclude the profile of the user making the request
            queryset = queryset.exclude(user=user)
        return queryset

    @action(detail=False, methods=['GET'], permission_classes=[permissions.IsAuthenticated])
    def my_profile(self, request):
        profile = UserProfile.objects.get(user=request.user)
        serializer = self.get_serializer(profile)
        return Response(serializer.data)