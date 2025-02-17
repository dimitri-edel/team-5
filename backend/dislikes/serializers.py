from rest_framework import serializers
from .models import Dislikes

class DislikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dislikes
        fields = ['id', 'user', 'disliked_profile', 'created_at']
