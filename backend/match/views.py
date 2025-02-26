from rest_framework import viewsets, permissions, status
from rest_framework.decorators import action
from rest_framework.response import Response
from user_profile.models import UserProfile
from user_profile.serializers import UserProfileSerializer
from .models import Match
from .serializers import MatchSerializer
from .permissions import Matched

class MatchViewSet(viewsets.ModelViewSet):
    queryset = Match.objects.all()
    serializer_class = MatchSerializer
    permission_classes = [permissions.IsAuthenticated, Matched]

    # List profiles that the user has matched with, i.e. user1 or user2
    @action(detail=False, methods=["GET"])
    def profiles(self, request):
        user_profile = UserProfile.objects.get(user=request.user)
        matches = Match.objects.filter(user1=user_profile) | Match.objects.filter(user2=user_profile)
        # Get the profiles of the users that the user has matched with,
        # excluding the user's own profile

        profiles = []
        for match in matches:
            if match.user1 == user_profile:
                profiles.append(match.user2)
            else:
                profiles.append(match.user1)

        serializer = UserProfileSerializer(profiles, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    # Flat list of profile ids that the user has matched with
    @action(detail=False, methods=["GET"])
    def profile_ids(self, request):
        user_profile = UserProfile.objects.get(user=request.user)
        matches = Match.objects.filter(user1=user_profile) | Match.objects.filter(user2=user_profile)
        # Get the profiles of the users that the user has matched with,
        # excluding the user's own profile

        profile_ids = []
        for match in matches:
            if match.user1 == user_profile:
                profile_ids.append(match.user2.profile_id)
            else:
                profile_ids.append(match.user1.id)

        return Response(profile_ids, status=status.HTTP_200_OK)