from rest_framework import permissions
from user_profile.models import UserProfile

class Matched(permissions.BasePermission):
    """
    Custom permission to only allow users who are part of the match to access the object.
    """

    def has_object_permission(self, request, view, obj):
        user_profile = UserProfile.objects.get(user=request.user)
        # Check if the user is either obj.user1 or obj.user2
        return obj.user1 == user_profile or obj.user2 == user_profile
