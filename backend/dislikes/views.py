from django.shortcuts import render
from rest_framework import viewsets, permissions
from .models import Dislikes
from .serializers import DislikeSerializer
from user_profile.models import UserProfile
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status
from .permissions import IsOwner

class DislikeViewSet(viewsets.ModelViewSet):
    queryset = Dislikes.objects.all()
    serializer_class = DislikeSerializer
    permission_classes = [IsOwner]

    @action(detail=True, methods=['POST'])
    def dislike(self, request, pk=None):
        '''Dislike a user profile
        If the user has not disliked the profile, create a dislike object
        If the user has disliked the profile, delete the dislike object
        '''
        profile = UserProfile.objects.get(pk=pk)
        request_user_profile = UserProfile.objects.get(user=request.user)
        dislike, created = Dislikes.objects.get_or_create(user=request_user_profile, dislikes=profile)
        if created:            
            return Response(status=status.HTTP_201_CREATED)
        elif dislike:
            try:                    
                dislike.delete()
                return Response(status=status.HTTP_204_NO_CONTENT)
            except Dislikes.DoesNotExist:
                return Response(status=status.HTTP_404_NOT_FOUND)
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    @action(detail=False, methods=['GET'])
    def disliked_profiles(self, request):
        '''Get a list of the primary keys of profiles that the user has disliked'''
        user_profile = UserProfile.objects.get(user=request.user)
        disliked_profiles = Dislikes.objects.filter(user=user_profile).values_list('dislikes', flat=True)
        return Response(disliked_profiles)