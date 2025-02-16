from rest_framework import serializers
from .models import UserProfile

class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = [
            'profile_id', 'user', 'display_name', 'age', 'is_online',
            'bio', 'avatar_image', 'gender', 'sexual_orientation',
            'country', 'city', 'contact', 'interests', 'other_details',
            'created_at', 'updated_at'
        ]
        read_only_fields = ['profile_id', 'created_at', 'updated_at'] 