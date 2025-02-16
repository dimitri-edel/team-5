from rest_framework import viewsets, permissions, status
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Like
from .serializers import LikeSerializer
from user_profile.models import UserProfile

class LikeViewSet(viewsets.ModelViewSet):
    queryset = Like.objects.all()
    serializer_class = LikeSerializer
    permission_classes = [permissions.IsAuthenticated]

    @action(detail=True, methods=['POST'])
    def like(self, request, pk=None):
        profile = UserProfile.objects.get(pk=pk)
        like, created = Like.objects.get_or_create(user=request.user.userprofile, likes=profile)
        if created:
            return Response(status=status.HTTP_201_CREATED)
        return Response(status=status.HTTP_200_OK)

    @action(detail=True, methods=['POST'])
    def unlike(self, request, pk=None):
        profile = UserProfile.objects.get(pk=pk)
        try:
            like = Like.objects.get(user=request.user.userprofile, likes=profile)
            like.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Like.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)


