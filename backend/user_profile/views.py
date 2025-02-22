from rest_framework import viewsets, permissions
from django_filters import rest_framework as filters
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import UserProfile
from .serializers import UserProfileSerializer
from .filters import UserProfileFilter

class UserProfileViewSet(viewsets.ModelViewSet):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = UserProfileFilter

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