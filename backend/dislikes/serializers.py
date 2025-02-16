from rest_framework import serializers
from .models import Dislike

class DislikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dislike
        fields = ['id', 'user', 'disliked_profile', 'created_at']
