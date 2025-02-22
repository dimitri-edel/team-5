from rest_framework import viewsets, permissions
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
        queryset = UserProfile.objects.all()
        if self.action == 'list':
            country = self.request.query_params.get('country', None)
            if country:
                queryset = queryset.filter(country=country)
        return queryset

    @action(detail=False, methods=['GET'])
    def my_profile(self, request):
        profile = UserProfile.objects.get(user=request.user)
        serializer = self.get_serializer(profile)
        return Response(serializer.data)

    @action(detail=False, methods=['GET'])
    def list_profiles(self, request):
        queryset = self.filter_queryset(self.get_queryset())
        paginator = self.pagination_class()
        result_page = paginator.paginate_queryset(queryset, request)
        response_data = [
            {
                "display_name": profile.display_name,
                "avatar_image": profile.avatar_image.url if profile.avatar_image else None,
                "age": profile.age,
            }
            for profile in result_page
        ]
        return paginator.get_paginated_response(response_data)