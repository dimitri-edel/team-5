from rest_framework import viewsets, permissions, generics
from django_filters import rest_framework as filters
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.pagination import PageNumberPagination
from .models import UserProfile
from .serializers import UserProfileSerializer
from .filters import UserProfileFilter
from .pagination import UserProfilePagination
from .permissions import IsOwner  # Import the custom permission
import logging

logger = logging.getLogger(__name__)

class UserProfileViewSet(viewsets.ModelViewSet):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = UserProfileFilter
    pagination_class = UserProfilePagination

    def create(self, request, *args, **kwargs):        
        response = super().create(request, *args, **kwargs)        
        return response

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

    def update(self, request, *args, **kwargs):
        self.permission_classes = [permissions.IsAuthenticated, IsOwner]
        self.check_permissions(request)
        return super().update(request, *args, **kwargs)

    def destroy(self, request, *args, **kwargs):
        self.permission_classes = [permissions.IsAdminUser]
        self.check_permissions(request)
        return super().destroy(request, *args, **kwargs)