from rest_framework import viewsets, permissions, status
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Like
from .serializers import LikeSerializer
from user_profile.models import UserProfile
from match.models import Match
from .permissions import IsOwner

class LikeViewSet(viewsets.ModelViewSet):
    queryset = Like.objects.all()
    serializer_class = LikeSerializer

    def get_permissions(self):
        if self.action == 'notifications':
            self.permission_classes = [permissions.IsAuthenticated]
        else:
            self.permission_classes = [IsOwner]
        return super().get_permissions()

    @action(detail=True, methods=['POST'])
    def like(self, request, pk=None):
        profile = UserProfile.objects.get(pk=pk)
        request_user_profile = UserProfile.objects.get(user=request.user)
        like, created = Like.objects.get_or_create(user=request_user_profile, likes=profile)
        if created:            
            return Response(status=status.HTTP_201_CREATED)
        elif like:
            # Check if the liked user has also liked the current user
            if Like.objects.filter(user=profile, likes=request_user_profile).exists():
                # Create a match
                Match.objects.create(user1=request_user_profile, user2=profile)
                return Response({"message": "Match created!"}, status=status.HTTP_201_CREATED)            
            else: # Unlike the user
                try:                    
                    like.delete()
                    return Response(status=status.HTTP_204_NO_CONTENT)
                except Like.DoesNotExist:
                    return Response(status=status.HTTP_404_NOT_FOUND)
        return Response(status=status.HTTP_404_NOT_FOUND)

    @action(detail=False, methods=['GET'])
    def notifications(self, request):
        request_user_profile = UserProfile.objects.get(user=request.user)
        notifications = Like.objects.filter(likes=request_user_profile)
        serializer = self.get_serializer(notifications, many=True)
        return Response(serializer.data)


